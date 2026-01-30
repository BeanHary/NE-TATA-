################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## 对话屏幕 ########################################################################
##
## 对话屏幕用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此屏幕必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#say

screen say(who, what):

    # 滚轮上滑打开历史界面
    key "mousedown_4" action ShowMenu("history")

    # ctrl键强制快进
    key "keydown_K_LCTRL" action [Preference("skip", "toggle")]
    key "anyrepeat_keyup_K_LCTRL" action [Preference("skip", "toggle")]
    key "keydown_K_RCTRL" action [Preference("skip", "toggle")]
    key "anyrepeat_keyup_K_RCTRL" action [Preference("skip", "toggle")]


    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style ruby_style is default:
    size 15
    yoffset -35 # PC设置为-35，Android设置为-45较合适
    color None 

style window is default
style say_label is default
style say_dialogue is default:
    ruby_line_leading 15
    ruby_style style.ruby_style
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    

    adjust_spacing False

## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("读取") action ShowMenu('load')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            if persistent.chapter_menu_active:
                textbutton _("开始游戏") action Show("chapter_menu")
            else:
                textbutton _("开始游戏") action Start()
        else:
            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取") action ShowMenu("load")

        # 对不同的设备，music_room将启用不同的布局
        if persistent.music_room_active and main_menu:
            if renpy.variant("pc"):
                textbutton "鉴赏" action ShowMenu("music_room")
            elif renpy.variant("mobile"):
                textbutton "鉴赏" action ShowMenu("music_room_android")
            
        if persistent.dictionary_active:

            textbutton "词典" action ShowMenu("dictionary")

        textbutton _("设置") action ShowMenu("preferences")

        # textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必需或相关。
            textbutton _("帮助") action ShowMenu("help")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()

        if renpy.variant("pc") and main_menu:

            ## 退出按钮在 iOS 上是被禁止使用的，在安卓和网页上也不是必要的。
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#main-menu
screen main_menu():

    ## 此语句可确保替换掉任何其他菜单屏幕。
    tag menu

    # 根据游戏是否通关来选择不同的背景
    if persistent.game_completed:
        add "gui/end_menu.png"  # 通关后的背景图片
    else:
        add gui.main_menu_background  # 默认背景

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    ## use 语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    font "YouShiSanGeng.ttf"
    color "#f18aca"
    bold True

style main_menu_version:
    properties gui.text_properties("version")
    font "YouShiSanGeng.ttf"
    bold True


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。可使用屏幕标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。此屏幕旨在与一个或多个子
## 屏幕同时使用，这些子屏幕将被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此屏幕没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义屏
## 幕。

screen about():

    tag menu

    ## 此 use 语句将 game_menu 屏幕包含到了这个屏幕内。子级 vbox 将包含在
    ## game_menu 屏幕的 viewport 内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## gui.about 通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个屏
## 幕都是以第三个屏幕 file_slots 来实现的。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#save https://doc.renpy.cn/zh-
## CN/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "K_DELETE" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) 给出 1 到 9 之间的数字。
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

#                if config.has_sync:
#                    if CurrentScreenName() == "save":
#                        textbutton _("上传同步"):
#                            action UploadSync()
#                            xalign 0.5
#                    else:
#                        textbutton _("下载同步"):
#                            action DownloadSync()
#                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## 设置屏幕 ########################################################################
##
## 设置屏幕允许用户配置游戏，使其更适合自己。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#preferences 

screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("快进模式")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

                ## 可在此处添加 radio_pref 或 check_pref 类型的额外 vbox，以添加
                ## 额外的创建者定义的偏好设置。

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动前进时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史屏幕 ########################################################################
##
## 这是一个向用户显示对话历史的屏幕。虽然此屏幕没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://doc.renpy.cn/zh-CN/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果 history_height 为 None 时仍可正常显示条目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置了
                        ## 的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("尚无对话历史记录。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text:
    ruby_line_leading 15
    ruby_style style.ruby_style

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5



## 影片屏幕 ########################################################################
##
## 这是一个向用户播放影片的屏幕。
$ movie_length = 0
$ skip_hide = 5.0
$ movie_playing = "None"

screen movie:
    
    add Movie(size=(1920,1080))
    on "show" action [Play("movie", movie_playing, loop=False), SetVariable('quick_menu', False)]
    on "hide" action [Stop("movie"), SetVariable('quick_menu', True)]
    
    timer 0.1 repeat True action If(movie_length > 0.0, true=(SetVariable('movie_length', movie_length - 0.1)), false=(Return(0)))

    timer 0.1 repeat True action If(skip_hide > 0.0, true=(SetVariable('skip_hide', skip_hide - 0.1)), false=(SetVariable('skip_hide', 0)))
    
    if skip_hide and persistent.game_completed:
        textbutton "跳过视频":
            action [Return(0), SetVariable('quick_menu', True)]
            sensitive (not renpy.get_screen("say"))
            align (.95,.95)
            at skip_fade

transform skip_fade:
    alpha 1.0 
    easein 5.0 alpha 0.0





## 章节选择屏幕 ########################################################################
##
## 这是一个向用户展示章节的屏幕。
transform menu_transform:
    alpha 0.0
    ease 1.0 alpha 1.0 

transform button_chapter1_transform:
    pos (1021, 577)
    anchor (0, 0)
    zoom (469.0 / 329.0)
    alpha 0.0
    pause 1.0
    ease 0.5 alpha 1.0 

transform button_chapter2_transform:
    pos (149, 71)
    anchor (0, 0)
    zoom (361.0 / 257.0)
    alpha 0.0
    pause 1.5
    ease 0.5 alpha 1.0 

transform button_chapter3_1_transform:
    pos (281, 586)
    anchor (0, 0)
    zoom (363.0 / 260.0)
    alpha 0.0
    pause 1.8
    ease 0.5 alpha 1.0 

transform button_chapter3_2_transform:
    pos (599, 202)
    anchor (0, 0)
    alpha 0.0
    pause 2.0
    ease 0.5 alpha 1.0 

transform button_chapter4_transform:
    pos (1154, 33)
    anchor (0, 0)
    zoom (573.0 / 398.0)
    alpha 0.0
    pause 3.0
    ease 0.5 alpha 1.0 

transform tooltip_transform:
    on show:
        alpha 0.0
        ease 0.2 alpha 1.0
    on hide:
        ease 0.2 alpha 0.0

screen tooltip(text):
    zorder 100
    text text:
        size 30
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
        xalign 0.5
        yalign 0.9
        at tooltip_transform

screen chapter_menu():
    tag menu

    # 右键返回标题界面
    key "mousedown_3" action ShowMenu("main_menu")

    add "gui/main_menu.png"

    add "gui/chapter_menu.png" at menu_transform

    textbutton "返回标题界面":
        pos (100, 1000)
        text_size 40
        action ShowMenu("main_menu")

    textbutton "" id "tooltip" style "tooltip_text"

    imagebutton:
        idle "gui/button/chapter1_idle.png" 
        hover "gui/button/chapter1_hover.png" 
        at [button_chapter1_transform]
        hovered Show("tooltip", text="§Chapter１ 节操屹立于大地之上")
        unhovered Hide("tooltip")
        action Start()

    imagebutton:
        idle "gui/button/chapter2_idle.png" 
        hover "gui/button/chapter2_hover.png" 
        at [button_chapter2_transform]
        hovered Show("tooltip", text="§Chapter２ 她的呼吸、她的体温")
        unhovered Hide("tooltip")
        action Start("FATE")

    if persistent.music_room_active:
        imagebutton:
            idle "gui/button/chapter3_1_idle.png" 
            hover "gui/button/chapter3_1_hover.png" 
            at [button_chapter3_1_transform]
            hovered Show("tooltip", text="§Chapter３.１ 家有女儿")
            unhovered Hide("tooltip")
            action Start("HACKER")
    else:
        imagebutton: 
            idle "gui/button/chapter3_1_idle.png" 
            hover "gui/button/chapter3_1_unlocked.png" 
            at [button_chapter3_1_transform]
            action NullAction()


    if persistent.music_room_active:
        imagebutton:
            idle "gui/button/chapter3_2_idle.png" 
            hover "gui/button/chapter3_2_hover.png" 
            at [button_chapter3_2_transform]
            hovered Show("tooltip", text="§Chapter３.２ 家有女儿")
            unhovered Hide("tooltip")
            action Start("ADULT")
    else:
        imagebutton: 
            idle "gui/button/chapter3_2_idle.png" 
            hover "gui/button/chapter3_2_unlocked.png" 
            at [button_chapter3_2_transform]
            action NullAction()


    if persistent.dictionary_active:
        imagebutton:
            idle "gui/button/chapter4_idle.png" 
            hover "gui/button/chapter4_hover.png" 
            hovered Show("tooltip", text="§Chapter４ 淌着奶与蜜之地")
            unhovered Hide("tooltip")
            at [button_chapter4_transform]
            action Start("SEX")
    else:
        imagebutton: 
            idle "gui/button/chapter4_idle.png" 
            hover "gui/button/chapter4_unlocked.png" 
            at [button_chapter4_transform]
            action NullAction()



## 鉴赏屏幕 ########################################################################
##
## 这是一个向用户展示音乐的屏幕。

init python:

    # Step 1. 创建一个MusicRoom实例。
    mr = MusicRoom(fadeout=1.0)

    # Step 2. 添加音乐文件。
    mr.add("music/winter.mp3")
    mr.add("music/spring.mp3")
    mr.add("music/wonderful time.mp3")
    mr.add("music/woman.mp3")
    mr.add("music/obituary.mp3")
    mr.add("music/sentence know.mp3")
    mr.add("music/daily1.mp3")
    mr.add("music/daily2.mp3")
    mr.add("music/sky.mp3")
    mr.add("music/a little happiness.mp3")
    mr.add("music/happiness is everywhere.mp3")
    mr.add("music/wall.mp3")
    mr.add("music/play with.mp3")
    mr.add("music/devil whisper.mp3")
    mr.add("music/white.mp3")
    mr.add("music/what comes into being.mp3")
    mr.add("music/last lament.mp3")
    mr.add("music/kotatsu.mp3")

    mr.add("music/kantai collection.mp3")
    mr.add("music/to the beginning.mp3")
    mr.add("music/never give up.mp3")
    mr.add("music/op A.mp3", always_unlocked=True)
    mr.add("music/op B.mp3", always_unlocked=True)
    mr.add("music/ed.mp3", always_unlocked=True)
    mr.add("music/extra ed.mp3", always_unlocked=True)


# 创建播放按钮类
    class PlayerButton:
        def __init__(self, channel='music', mr=mr):
            self.channel = channel
            self.mr = mr
            self.is_muted = False

        def get_text(self):
            if not renpy.music.is_playing() and not renpy.music.get_pause():
                return "▶"  
            if renpy.music.get_pause(self.channel):
                return "▶"  
            return "⏸"     

        def click(self):
            if not renpy.music.is_playing() and not renpy.music.get_pause():
                self.mr.play()
                return
            renpy.music.set_pause(not renpy.music.get_pause(self.channel),
                channel=self.channel)
        
        def toggle_mute(self):
            self.is_muted = not self.is_muted
            if self.is_muted:
                _preferences.set_volume("music", 0.0)
            else:
                _preferences.set_volume("music", 1.0)

    # 创建按钮实例
    play_button = PlayerButton(mr=mr)

# Step 3.1 创建音乐空间界面（PC）
screen music_room:

    tag menu

    add "gui/music_room.png"

    # 右键返回标题界面
    key "mousedown_3" action ShowMenu("main_menu")

    frame:
        background None

        has vbox

        hbox:
            vbox:
        # 每条音轨的播放按钮。
                textbutton "卢明俊 - 冬" action mr.Play("music/winter.mp3")
                textbutton "卢明俊 - 春" action mr.Play("music/spring.mp3")
                textbutton "曾志豪 - 美好时光" action mr.Play("music/wonderful time.mp3")
                textbutton "贵族乐团 - 善变的女人" action mr.Play("music/woman.mp3")
                textbutton "Alexandre Desplat - Obituary" action mr.Play("music/obituary.mp3")
                textbutton "のる - どんぐりみいつけた" action mr.Play("music/daily2.mp3")
                textbutton "のる - 空を見上げて" action mr.Play("music/sky.mp3")
                textbutton "TinyMemory - A little happiness" action mr.Play("music/a little happiness.mp3")
                textbutton "TinyMemory - Happiness is everywhere" action mr.Play("music/happiness is everywhere.mp3")

                null height 50

                textbutton "AKINO from bless4 - みいろ" action mr.Play("music/kantai collection.mp3")
                textbutton "Kalafina - To the beginning" action mr.Play("music/to the beginning.mp3")
                textbutton "ZARD - 负けないで" action mr.Play("music/never give up.mp3")
                textbutton "川村ゆみ - Moving go on" action mr.Play("music/op A.mp3")
                textbutton "大原ゆい子 - 言わないけどね。" action mr.Play("music/op B.mp3")
                textbutton "邓丽君 - 我只在乎你" action mr.Play("music/ed.mp3")
                textbutton "イケてるハーツ - 罪証のルシファー" action mr.Play("music/extra ed.mp3")

            null width 20

            vbox:
                textbutton "えびかれー伯爵 - Sentence know" action mr.Play("music/sentence know.mp3")
                textbutton "ゆうり - 越えられない壁" action mr.Play("music/wall.mp3")
                textbutton "ゆうり - ゆるくいこうよ" action mr.Play("music/daily1.mp3")
                textbutton "Fukagawa - うまくいくかね？" action mr.Play("music/play with.mp3")
                textbutton "ハシマミ - Devil's whisper" action mr.Play("music/devil whisper.mp3")
                textbutton "KOTATSU!! - えだまめ88" action mr.Play("music/kotatsu.mp3")
                textbutton "yuhei komatsu - white" action mr.Play("music/white.mp3")
                textbutton "Heitaro Ashibe - What comes into being" action mr.Play("music/what comes into being.mp3")
                textbutton "Marron Fields Production - Last Lament" action mr.Play("music/last lament.mp3")

                null height 175

                hbox:
                    xalign 0.48
                    textbutton "返回标题界面" action ShowMenu("main_menu") 

                hbox:
                    xalign 0.5  
                    textbutton "⏮" action mr.Previous()
                    null width 20
                    textbutton play_button.get_text(): 
                        action Function(play_button.click)
                    null width 20
                    textbutton "⏭" action mr.Next()
                    null width 20

                hbox:
                    if config.has_music: 
                        if not play_button.is_muted and preferences.get_mixer("music")!=0:
                            textbutton "🔊" action Function(play_button.toggle_mute)
                        else:
                            textbutton "🔈" action Function(play_button.toggle_mute)   
                        null width 10
                        bar value Preference("music volume") xsize 500 yalign 0.5
                            
    # 音乐空间的音乐播放入口。
    on "replace" action mr.Play()

    # 离开时恢复主菜单的音乐。
    on "replaced" action Play("music", "music/winter.mp3")



# Step 3.2 创建音乐空间界面（Android）

screen music_room_android:

    tag menu

    add "gui/music_room.png"

    # 右键返回标题界面
    key "mousedown_3" action ShowMenu("main_menu")

    frame:
        background None

        has vbox

        hbox:
            vbox:
        # 每条音轨的播放按钮。
                textbutton "卢明俊 - 冬" action mr.Play("music/winter.mp3")
                textbutton "卢明俊 - 春" action mr.Play("music/spring.mp3")
                textbutton "曾志豪 - 美好时光" action mr.Play("music/wonderful time.mp3")
                textbutton "贵族乐团 - 善变的女人" action mr.Play("music/woman.mp3")
                textbutton "Alexandre Desplat - Obituary" action mr.Play("music/obituary.mp3")
                textbutton "のる - どんぐりみいつけた" action mr.Play("music/daily2.mp3")
                textbutton "のる - 空を見上げて" action mr.Play("music/sky.mp3")
                textbutton "TinyMemory - A little happiness" action mr.Play("music/a little happiness.mp3")
                textbutton "TinyMemory - Happiness is everywhere" action mr.Play("music/happiness is everywhere.mp3")

                

                textbutton "AKINO from bless4 - みいろ" action mr.Play("music/kantai collection.mp3")
                textbutton "Kalafina - To the beginning" action mr.Play("music/to the beginning.mp3")
                textbutton "ZARD - 负けないで" action mr.Play("music/never give up.mp3")
                textbutton "川村ゆみ - Moving go on" action mr.Play("music/op A.mp3")
                
                

            null width 20

            vbox:
                textbutton "えびかれー伯爵 - Sentence know" action mr.Play("music/sentence know.mp3")
                textbutton "ゆうり - 越えられない壁" action mr.Play("music/wall.mp3")
                textbutton "ゆうり - ゆるくいこうよ" action mr.Play("music/daily1.mp3")
                textbutton "Fukagawa - うまくいくかね？" action mr.Play("music/play with.mp3")
                textbutton "ハシマミ - Devil's whisper" action mr.Play("music/devil whisper.mp3")
                textbutton "KOTATSU!! - えだまめ88" action mr.Play("music/kotatsu.mp3")
                textbutton "yuhei komatsu - white" action mr.Play("music/white.mp3")
                textbutton "Heitaro Ashibe - What comes into being" action mr.Play("music/what comes into being.mp3")
                textbutton "Marron Fields Production - Last Lament" action mr.Play("music/last lament.mp3")

                
                textbutton "大原ゆい子 - 言わないけどね。" action mr.Play("music/op B.mp3")
                textbutton "邓丽君 - 我只在乎你" action mr.Play("music/ed.mp3")
                textbutton "イケてるハーツ - 罪証のルシファー" action mr.Play("music/extra ed.mp3")

                

                hbox:
                    xalign 0.48
                    textbutton "返回标题界面" action ShowMenu("main_menu") 

                
                     
                    textbutton "⏮" action mr.Previous()
                    null width 20
                    textbutton play_button.get_text(): 
                        action Function(play_button.click)
                    null width 20
                    textbutton "⏭" action mr.Next()
                    null width 20

                
                    if config.has_music: 
                        if not play_button.is_muted and preferences.get_mixer("music")!=0:
                            textbutton "🔊" action Function(play_button.toggle_mute)
                        else:
                            textbutton "🔈" action Function(play_button.toggle_mute)   
                        null width 10
                        bar value Preference("music volume") xsize 200 yalign 0.5
                            
    # 音乐空间的音乐播放入口。
    on "replace" action mr.Play()

    # 离开时恢复主菜单的音乐。
    on "replaced" action Play("music", "music/winter.mp3")



## 词典屏幕 ########################################################################
##
## 这是一个向用户展示tips的屏幕。

init python:
    # 定义所有tips
    tips_data = [
        {
            "title": "暨珠学运与青工办",
            "content": "　　全称“暨南大学珠海校区学生运动与青年工作办公室（the Student Movement and Youth Work Office of Jinan University Zhuhai Campus）”，目标是——解放全人类！然而实际上既不是暨南大学下属的行政单位，也不是官方认证的学生社团。{p}　　“这没关系，”许○○如是说：“早晚有一天世人会认可我们孤傲而崇高的理想的。”林笃只是在一边苦笑着摇了摇头。"
        },
        {
            "title": "神粥",
            "content": "　　于深圳建立的一所IT企业，曾以4000~5000元价位的低廉准系统笔记本电脑而闻名，十年前流传着“减钱上船”的说法，受到众多电脑爱好者的追捧——甚至当时专门创造了“粥批”一词用于称呼其粉丝群体。{p}　　后因多种原因逐渐衰落，如今其在性价比品牌中的市场地位已被另一公司“机器革命”所取代。"
        },
        {
            "title": "玫瑰战争",
            "content": "　　原型为1455年－1485年英国王室继承人为争夺王位而发生的内战。在“主线”中，许○○把从未来的四大元老手里夺回林笃的作战命名为“玫瑰战争”。"
        },
        {
            "title": "国补",
            "content": "　　国家补贴，是根据政策需要，由财政部门实施的对某些特定的产业、部门、地区、企事业单位或某些特定的产品、事项给予的补贴和津贴。{p}　　更准确地说，这里指的是2025年的消费品以旧换新补贴，各省在拨款资金额度内发放补贴，消费者在购买家电等产品时可享受一定程度的优惠。本意为拉动整体消费水平，为上游供应链创造新的增量，但在实际执行过程中，套补、骗补现象层出不穷，加之地方财政枯竭，被人怀疑是官商勾结的白手套。"
        },
        {
            "title": "现充",
            "content": "　　来自于日本的二次元网络用语，指现实生活中享受人际关系和爱好活动，而无需互联网路上的博客和SNS就能过得很充实的人，是由日本网络论坛5ch发祥的网络俚语，近年来，有恋人有无的规定倾向。"
        },
        {
            "title": "负能量",
            "content": "　　在物理学中，负能量特指一种量子效应产生的、能量密度低于经典真空（零点能）的状态，是一种由量子涨落（如卡西米尔效应）在特定条件下产生的微观现象，被认为拥有支撑虫洞喉部保持开放实现时间旅行的潜力。"
        },
        {
            "title": "史塔西虫洞",
            "content": "　　在“主线”中，许○○把“史瓦西黑洞”同东德的“史塔西”相混淆闹出的笑话，后来用于命名部署在GitHub服务器上的数字黑洞-虫洞模型。{p}　　虫洞部分置于黑洞周围的强引力环境之中，从而制造时间差。因为是计算机模拟的结果所以克服了实际操作中复合镶嵌的困难。"
        },
        {
            "title": "地球OL",
            "content": "　　地球OnLine，把现实比作游戏的一种网络说法。"
        },
        {
            "title": "BBS",
            "content": "　　电子布告栏系统（Bulletin Board System）,网络论坛的前身。"
        },
        {
            "title": "DQN",
            "content": "　　流行于10年代左右的日本网络用语，一般指头脑不好、缺乏常识或轻易使用暴力的人，可以简单理解成汉语里的“神经病”“脑子有坑”。{p}　　事实上，DQN该词从未真正传入中文互联网，在如今的日本也几乎成了死语，这里作为对PC游戏『Chaos;Head』的彩蛋出现。随着游戏推进，你将会看到更多与科学ADV系列相关的致敬（倒不如说许多地方就是照抄……嗯，作者缺乏从零创作的能力）。{p}　　请注意：出于各种原因，词典只会解释少数较生涩的neta。因为……笑点解析出来就不好笑了嘛！"
        },
        {
            "title": "V信",
            "content": "　　V信（VChat）是一款来自中国的国民级即时通讯软件，月活跃用户数超过１４亿，图标为一个置于绿底的白色大写英文字母Ｖ。{p}　　用户可以在上面免费地聊天、打电话、发红包、玩小游戏等，其中最有名的功能——朋友圈，允许你随心地向身边的好友分享生活、转发推文，被网络上一部分人认为是现充必备。"
        },
        {
            "title": "galgame",
            "content": "　　美少女游戏，或称galgame、黄油（在通常语境下不作严格区分），是一种来自日本的可以与动画美少女进行互动的电子游戏。{p}　　大部分美少女游戏涉及爱情、性交或者某种形式的性暗示，由于中国特殊的压抑国情，近年来galgame在短视频平台不断走红，使得越来越多的日本厂商愈发重视海外市场的同时也引发了一部分老人和新人之间的观念冲突。"
        },
        {
            "title": "HS",
            "content": "　　galgame的黄色情景（H Scene）。经常见到有人误以为“HS”是中文“黄色”的全拼缩写，尽管过程错了但答案全对……真是微妙。{p}　　一般来说，以有无HS作为区分全年龄或成人向的标志。但如今受到业界衰微的影响，相当一部分黄油厂商对HS相当敷衍，要么插入突兀，要么毫无实用性。令人感叹。"
        },
        {
            "title": "薄纱",
            "content": "　　“爆杀”的谐音，主要用于网络交流。"
        },
        {
            "title": "百do",
            "content": "　　一家主营搜索引擎的科技企业，与阿巴阿巴、鹅厂合称为中国互联网三大巨头。{p}　　其核心产品有“百do搜索”“百do贴贴吧”等，在胡歌（hoogle）退出中国市场后取得了事实上的垄断地位，但其用户体验、商业模式等方面历来饱受诟病。"
        },
        {
            "title": "MC",
            "content": "　　官方中文译名《我的手艺活》（Mycraft），一款风靡世界的高自由度沙盒冒险游戏，与《饱慌》、《太拉了呀》合称生存游戏三巨头。{p}　　作为全球销量最高的游戏，在中国保持着不温不火的热度。虽然游戏长久不衰的生命力主要来自模组社区，但近年官方疲软的更新也引起了一部分玩家的不满。"
        },
        {
            "title": "草肚皮",
            "content": "　　中国古代围棋有句话叫“金角银边草肚皮”，也是许多围棋新人的必修课，指棋子在不同位置围空效率的差异，优先占据角部和边部的策略。{p}　　“草肚皮”之所以被视为“草”，是因为中央地域四面受敌、难以固守；而“金角”“银边”则可凭借棋盘边缘为天然屏障，易守难攻。一旦在边角站稳并形成合围，中央之势便难以生存。这一战术思维，与中国古代“韬光养晦、后发制人”的军事智慧不谋而合。"
        },
        {
            "title": "圆明新园",
            "content": "　　（未作和谐处理）珠海市石景山下的主题公园，“珠海十景”之一。{p}　　号称模仿北京圆明园一比一建造——不过也只是再现了一部分建筑而已。"
        },
        {
            "title": "安全裤",
            "content": "　　足以名列许○○心目中世上最傻逼物件前十的选手，是一种以防止走光为主要功能的四角短裤类服饰。{p}　　许○○：“穿安全裤的角色为什么能被评为萌王？我根本萌不起来。”"
        },
        {
            "title": "轻小说",
            "content": "　　一种以“可轻松阅读”为目的的文艺作品，诞生于日本。{p}　　最初的轻小说与现在的轻小说相去甚远，不少文坛大咖也相当青睐这种体裁。随着市场化的推进，在今天，轻小说更多指的是ACGN中“N”的一环，形成了一套完整的产业体系。它们多以青少年为主要受众，配有动漫风格的插图，一卷在10万到20万字不等（物理上根本不轻！不如口袋本），人气轻小说还会被搬上电视荧幕改编为TV动画。{p}　　由于如今的轻小说质量参差不齐，人们常戏称为“厕纸”“买插画送小说”。"
        },
        {
            "title": "大和号",
            "content": "　　旧日本帝国海军所建造的最大一级战列舰，也是人类海军舰船史上最大的一级战列舰。大和号集结了当时日本最高的技术而建成，全舰覆盖大量装甲，还配备有最大的460毫米主炮，成为许多军迷心目中的究极浪漫。{p}　　然而，就是这样的海上钢铁巨兽，于1945年4月7日在冲绳岛战役中被美军飞机击沉，为一些军事宅所惋惜并视作“大舰巨炮时代的落幕”。"
        },
        {
            "title": "波动炮",
            "content": "　　出自动画《宇宙战舰大和号》（未作和谐处理），是大和号的超级武器，主要原理为放射超光速粒子流或放射高维空间来蒸发目标。"
        },
        {
            "title": "光明顶",
            "content": "　　金庸小说《倚天屠龙记》（未作和谐处理）中的地名，为中土「明教」总坛所在地，位于西域「昆仑山」。{p}　　小说中六大门派与明教素有恩怨，遂趁明教内部虚弱时结成同盟西征昆仑山，是为「六大门派围攻光明顶」，后因张无忌调停而罢兵。"
        },
        {
            "title": "3S政策",
            "content": "　　韩国总统全斗焕（未作和谐处理）上台后针对年轻人实施的愚民政策。其意在于通过Screen（电视或电影）、Sport（竞技运动）、Sex（性）让大众丧失政治和社会问题的兴趣，以维持政权稳定。{p}　　最终全斗焕迫于全国民主运动局势下台，宣告了3S政策的破产……了吗？"
        },
        {
            "title": "苏黎世联邦理工学院",
            "content": "　　瑞士在传统上被视为德意志文化圈的一部分，却并非典型的民族国家。其国家构建根植于联邦主义与民主体制，并以国际公认的“永久中立国”身份著称。{p}　　位于该国的苏黎世联邦理工学院（未作和谐处理），历史上曾涌现出阿尔伯特·爱因斯坦、沃尔夫冈·泡利等多位杰出科学家。这些学者往往兼具犹太裔背景，而瑞士本身特殊的中立国地位，使某些阴谋论者将其与所谓掌控全球的“犹太资本”相联系，甚至猜测这所学院是否扮演着某种不为人知的秘密角色。"
        },
        {
            "title": "尤里",
            "content": "　　游戏《红色警戒2》及《尤里的复仇》（未作和谐处理）中的角色。{p}　　设定里为斯大林培养出来的心灵控制专家，后来背叛苏联，建立了自己的阵营。尤里拥有控制他人心灵的能力，在战场上可以控制大部分意志薄弱的敌军部队，真身甚至可以将一整个建筑内的人都能控制住。"
        },
        {
            "title": "SSD",
            "content": "　　电脑有两种主流的长期存储设备，SSD（固态硬盘）和HDD（机械硬盘）。由于HDD读取慢，更适合台式机“冷存”长期不使用的数据，现在的笔记本已不再配有SATA接口。{p}　　固态颗粒分五种，无论从寿命还是性能来说，都是SLC>MLC>TLC>QLC>PLC。当然，与之水涨船高的还有成本，因此SLC和MLC在市面上几乎不可见，TLC成为了大多数人的SSD消费首选，QLC和PLC则被DIY爱好者们蔑称为“电子垃圾”。"
        },
        {
            "title": "RAM",
            "content": "　　更准确地说，这里指的是主流的DRAM（动态随机存取存储器），或者更通俗地讲，内存条。常见的规格有DDR4和DDR5。{p}　　欧泊瑟弗妖：为什么人类总是热衷于发明各种各样的词指代同一个东西创造认知门槛呢？"
        },
        {
            "title": "狗东",
            "content": "　　中国电子商务公司，主要为B2C模式的购物网站。{p}　　售后优良，但是，很贵。大多时候比许多第三方店铺还贵。看来即便是B2C也免不了中间商赚差价（笑）。"
        },
        {
            "title": "区块链",
            "content": "　　基于密码学与共识机制构建的点对点网络系统，起源于比特币的发明，具有良好的去中心化、不可篡改、透明、安全和可编程特征，一度被寄予厚望。{p}　　然而随着加密货币市场的暴跌与各类诈骗案件的频发，尤其是经历了炒币、矿潮等一系列全球性冲击事件后，区块链技术的实际应用价值与前景遭到广泛质疑，激进者甚至将其与“元宇宙”并列称为“庞氏骗局”。"
        },
        {
            "title": "CloudFlare",
            "content": "　　（未作和谐处理）一家以提供DDos保护、CDN加速和DNS解析为主要业务的美国科技公司。官方宣称每天拦截2340亿网络威胁，保护世界上约20%的网站。{p}　　历史上曾遭遇多次崩溃，不管怎么说，每次崩溃都是全球IT圈的一件大事。"
        },
        {
            "title": "⭐🦆🐜",
            "content": "　　星鸭蚁，即“性压抑”，为了规避平台审核而使用emoji代替汉字的一种社区黑话。{p}　　也称为“性饥饿”，是指人们因各种原因无法表现出自己性欲的生理和心理状态，严重的会引发失眠、恶梦、头晕等神经功能失调症状。{p}　　近年来随着简中互联网对性的解构，已经成为一种自嘲说法乃至网络模因。"
        },
        {
            "title": "四大元老",
            "content": "　　简称F4，原型为历史上的国民党四大元老张静江、蔡元培、吴稚晖、李石曾（未作和谐处理）。{p}　　许○○高中时期妄想的一个秘密掌控世界的地下组织，设有“元首”（江恬语）一位，终极目标不明。后来借由妄想周记化作了现实，控制着里世界和表世界的能量流动。{p}　　就连许○○本人也承认，其权力运行机制就像“过家家”一样，到2025年已名存实亡，但不知出于什么原因，它在2047年完成内部重组后再度活跃起来，启动了“萌化世界”战略，妄图塑造世界的单一xp。"
        }, 
        {
            "title": "⏰",
            "content": "　　闹钟，即“老中”，与“老美”相对，为了规避平台审核而使用emoji代替汉字的一种社区黑话。{p}　　类似的称呼还有东大、天朝、CN、印度、越南。"
        },
        {
            "title": "航÷",
            "content": "　　即“航畜”，为了规避平台审核而使用符号代替汉字的一种社区黑话。{p}　　因百do贴贴吧“航空母舰吧”整体意识形态偏粉红而得名。常被指代用以辱骂无脑爱国的网友。一般与“中国人口吧”的吧友对立。"
        },
        {
            "title": "神区",
            "content": "　　即“神蛆”，为了规避平台审核而使用谐音字代替的一种社区黑话。{p}　　起源于百do贴贴吧“神奈川冲浪里吧”，包含大量恨国、崇洋媚外言论，其用户被称作“神神”，显然，“神蛆”是对他们的贬义称呼。"
        },
        {
            "title": "85",
            "content": "　　“吧务”的简写。{p}　　百do贴贴吧的社区管理员，由“吧主”任命，具有删除帖子、封禁用户的权力。"
        },
        {
            "title": "十循永封",
            "content": "　　“十天循环永久封禁”的简写。{p}　　在百do贴贴吧，即使是吧主，最多也只能禁言用户十天，但封禁用户没有冷却时间限制，于是就可以通过脚本等手段循环十天禁言达到永久封禁的效果。{p}　　值得注意的是，这种行为一经举报就会被百do官方认作违规，历史上屡次发生管理团队因整治发言环境结果反被裁撤，引得大量广告狗麦片哥入侵的事件，作为百do不当人一面的冰山一角。"
        },
        {
            "title": "串子",
            "content": "　　特指互联网上反串的闹事者，亦用其谐音“帆船”的emoji“⛵”指代，通过反话正说、搬弄是非等手段激起路人愤怒，引发骂战，扰乱网络环境。{p}　　不过也有部分社交网站以串为特色，达成一种诙谐的效果，维持热度，保持人气。"
        },
        {
            "title": "等等党",
            "content": "　　主要用于数码圈，指那些不急着入手电子产品，采取“等”的策略以期厂商降价促销的人群。"
        },
        {
            "title": "阿瓦隆",
            "content": "　　噼里啪啦的控评系统。{p}　　早期噼里啪啦会将评论区敏感词自动替换成***。这种方法不联系语境，过于粗暴且极度依赖词库，常出现误封情况。阿瓦隆系统采用AI审核+人工复审的机制，AI会将不合适的评论提交后台，设置为仅用户自己可见，既使发言人难以发觉自己的评论被管控，也可以起到保护社区环境或者说控制舆论风向的作用。"
        },
        {
            "title": "噼里啪啦",
            "content": "　　通称批站，一个以ACG相关内容起家的弹幕视频分享网站，中国最大的年轻人聚集平台之一。{p}　　不断做大的同时，在营收策略、社区管理等方面出现了许多与早期方向不合的问题。大批宅宅对此感到非常不满，认为批站早已变质只是不倒。"
        },
        {
            "title": "笔电男大",
            "content": "　　“玩笔记本电脑的男大学生”的简写。{p}　　该称呼最初用于主机玩家与PC玩家之间的骂战，后来在ps5贴贴吧、大黑盒进一步扩大，这个词也成为不同平台、不同社群玩家矛盾的缩影之一。"
        },
        {
            "title": "人人点评",
            "content": "　　米团公司旗下的第三方消费点评网站。用户可在上面查询本地生活信息、消费优惠以及发布评价。"
        },
        {
            "title": "米团",
            "content": "　　一家主要提供诸如外卖、出行等生活服务的电子商务平台，自与人人点评网合并后加速了扩张的步伐，现涵盖的业务范围非常广。{p}　　与狗东、桃饱闪购合称外卖三巨头。他们家的APP是这三家里最臃肿的。"
        },
        {
            "title": "中二",
            "content": "　　全称“中二病”，也称“厨二病”，指青春期少年特有的自以为是的思想、行动和价值观。{p}　　伴随网络上的广泛使用，该词的意义也走向泛化，既有二次元意义上对“邪气眼”的形容，也有单纯对现实里人自我意识过盛、狂妄，又觉得不被理解、自觉不幸的吐槽。{p}　　林笃：“造句：江恬正处于这个年龄就算了，可是某人……嗯，中二了快半辈子还没见消退的迹象……”"
        },
        {
            "title": "尴尬癌",
            "content": "　　2010年代兴起的网络名词，特指因目睹他人或自身遭遇尴尬情境而产生强烈不适的心理反应。{p}　　心理学上，尴尬癌的专有名词叫“替代性尴尬”，与个体的共情能力高度相关。在社交媒体普及的背景下，该词成为“尬文化”（如尬舞、尬聊等）的重要组成部分，常被用于调侃明星表演浮夸、社交场合失态等情境。{p}　　江恬：“是的，换用个更摩登的说法吧，我的脚趾都替爸爸感到尴尬，已经在地上都抠出三室一厅了。”"
        },
        {
            "title": "Docker",
            "content": "　　一个社区开源应用，基于操作系统层级的虚拟化技术将软件与其依赖项打包为容器，从而使得不同容器中的应用程序彼此隔离，相比虚拟机更加便捷。"
        },
        {
            "title": "领域展开",
            "content": "　　日本动漫《肘术回战》的必杀技。{p}　　用咒力将生得领域具现化到现实中，并注入术式，构筑出施加了术式的生得领域，在领域内可以得到BUFF加成，同时发动施予领域的术式必定命中。发动需要充足的咒力、对结界术有极高的造诣以及对自身术式理解和掌握程度足够高，发动后术式会出现暂时的熔断。"
        },
        {
            "title": "洋葱路由",
            "content": "　　一种在电脑网络上匿名沟通的技术。应用这种技术，传递的数据包会被一层一层地加密、包装，因酷似洋葱而得名。{p}　　数据经由一系列洋葱路由器发送，每经过一个节点就会将数据包的最外层解密，直至目的地时将最后一层解密，目的地因而能获得原始消息。而因为透过这一系列的加密包装，每一个网络节点（包含目的地）都只能知道上一个节点的位置，但无法知道整个发送路径以及原发送者的地址，从而保持了高匿名性。"
        },
        {
            "title": "渗透测试",
            "content": "　　文明黑客对公司的安全基础设施进行有计划的攻击，以查找需要修补的安全漏洞，可以认为类似于一种演习。"
        },
        {
            "title":"中央俱乐部",
            "content": "　　谁是历史的推动者？社会主义者答人民，然而人民常常怠惰，惯于被动；谁来打破空转的历史周期律？民主主义者答人民，但人民往往失语，惯于缄默。{p}　　究竟何为“人民的选择”？所谓“人民的意志”由谁执行？人民是可以被蒙蔽的，人民是可以被代表的。It's our duty！这便是中央俱乐部——那群自居为“上·面·的·人”——代替人民发表的意见。{p}　　中央俱乐部，简称CC，以历史上掌管国民党党务的陈家兄弟为原型，汇聚五大洲的权贵政要、技官智囊建立的秘密集团，借早已解散的四大元老展开认知作战，以掩盖他们扑朔迷离的真实行动。{p}　　其存在横跨人类历史，超越时间概念。也许掷出窗外和玫瑰战争……一切皆在他们的计划之中？"
        }
    ]
    
    current_tip = 0

screen dictionary():
    tag menu
    
    use game_menu("词典"):
        
        hbox:
            # 左侧：tips列表
            frame:
                xsize 450
                ysize 750
                viewport:
                    id "vp"
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    vbox:
                        for i in range(len(tips_data)):
                            button:
                                xsize 430
                                # 高亮当前选中的tip
                                if SelectedIf:
                                    background "#333333"
                                else:
                                    background "#222222"
                                hover_background "#444444"
                                action [SetVariable("current_tip", i), SelectedIf(i == current_tip)]
                                text tips_data[i]["title"] style "button_text"
            
            # 右侧：tip详情
            frame:
                xsize 750
                ysize 750
                vbox:
                    text tips_data[current_tip]["title"] size 40 xalign 0.5
                    null height 20
                    text tips_data[current_tip]["content"] size 30





## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    hbox:

        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "F11"
        text _("全屏/窗口。")

    hbox:
        label "F12"
        text _("截图。")

    hbox:
        label _("Esc")
        text _("打开游戏菜单。")

    hbox:
        label _("Delete")
        text _("悬停时按下删除存档。")

    hbox:
        label _("Shift")
        text _("进入/退出快进模式。")

    hbox:
        label _("Ctrl")
        text _("按住时强制快进所有文本。")

    hbox:
        label _("Tab")
        text _("跳转至下一选项（与快进模式设置有关）。")

    hbox:
        label "Shift + A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("滚轮上滑")
        text _("打开对话历史。")

    hbox:
        label _("滚轮下滑")
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至后来的对话。")

    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导，B/右键")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认屏幕。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
    

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## skip_indicator 屏幕用于指示快进正在进行中。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://doc.renpy.cn/zh-CN/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#nvl


screen nvl(dialogue, items=None):

    # 滚轮上滑打开历史界面
    key "mousedown_4" action ShowMenu("history")

    # ctrl键强制快进
    key "keydown_K_LCTRL" action [Preference("skip", "toggle")]
    key "anyrepeat_keyup_K_LCTRL" action [Preference("skip", "toggle")]
    key "keydown_K_RCTRL" action [Preference("skip", "toggle")]
    key "anyrepeat_keyup_K_RCTRL" action [Preference("skip", "toggle")]


    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在 vpgrid 或 vbox 中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 显示菜单，如果给定的话。如果 config.narrator_menu 设置为 True，则菜单
        ## 可能显示不正确。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## 对话气泡屏幕 ######################################################################
##
## 对话气泡屏幕用于以对话气泡的形式向玩家显示对话。对话气泡屏幕的参数与 say 屏幕
## 相同，必须创建一个 id 为 what 的可视控件，并且可以创建 id 为 namebox、who 和
## window 的可视控件。
##
## https://doc.renpy.cn/zh-CN/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
