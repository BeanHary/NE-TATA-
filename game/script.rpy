## 如何构建Android版本：
#
# 1. script.rpy中所有角色定义的ctc参数改成ctc="ctc_blink_android"
# 2. screens.rpy中ruby_style的yoffset从-35改成-45

define r = Character("林笃", who_color="#f18aca", ctc="ctc_blink", ctc_position="nestled")

define w = Character("许○○", who_color="#d6ba8c", ctc="ctc_blink", ctc_position="nestled")

define R = Character("？？？", ctc="ctc_blink", ctc_position="nestled")

define RR = Character("？？？", kind=nvl)

define C = Character("大背头老师", who_color="#808080", ctc="ctc_blink", ctc_position="nestled")

define j = Character("江恬", who_color="#f2f547", ctc="ctc_blink", ctc_position="nestled")

define narrator = nvl_narrator

define adv = Character(ctc="ctc_blink", ctc_position="nestled")
# PC为ctc="ctc_blink"，Android为ctc="ctc_blink_android"

image ctc_blink:
    "gui/button/ctc.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat 

image ctc_blink_android:
    "gui/phone/button/ctc.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

image lindu unhappy:
    "images/lindu unhappy.png"
    zoom 500/240

image lindu doggy:
    "images/lindu doggy.png"
    zoom 500/303

image lindu shy:
    "images/lindu shy.png"
    zoom 500/742

image lindu ok:
    "images/lindu ok.png"
    zoom 500/480

image lindu angry:
    "images/lindu angry.png"
    zoom 500/398

image lindu satisfied:
    "images/lindu satisfied.png"
    zoom 500/466

image lindu amazed:
    "images/lindu amazed.jpg"
    zoom 500/673

image lindu jealous:
    "images/lindu jealous.jpg"
    zoom 500/246

image hammer:
    "images/hammer.jpg"
    zoom 0.3

image shirt:
    "images/shirt.jpg"
    zoom 0.35

image rain:
    "images/rain1.png"
    zoom 2.4
    0.2
    "images/rain3.png"
    zoom 2.4
    0.2
    "images/rain2.png"
    zoom 2.4
    0.2
    repeat

image bg family:
    "images/bg family.png"
    zoom 1920/812

image bg hometown:
    "images/bg hometown.png"
    zoom 1920/2030

image chapter1 complete = Text("章节《节操屹立于大地之上》已完成。", style="chapter_complete_text") 

image chapter2 complete = Text("章节《她的呼吸、她的体温》已完成。", style="chapter_complete_text") 

image chapter3 complete = Text("章节《家有女儿》已完成。", style="chapter_complete_text") 

image chapter4 complete = Text("章节《淌着奶与蜜之地》已完成。", style="chapter_complete_text") 

image fin = Text("- Fin -", style="chapter_complete_text") 
    
style chapter_complete_text:
    size 80
    bold True
    font "YouShiSanGeng.ttf"
    outlines [(2, "#000000", 0, 0)]
    

label splashscreen:

    scene black
    with Pause(1)

    show text "⚠️\n\n仅供内部交流学习使用，请勿进行任何形式的二次分发！\n这是一个日本全年龄美少女游戏。与现实中国没有任何联系。\n日语为本游戏的唯一官方语言。一切游戏内容均取材于日本：\n故事背景位于日本的中国地方，出场人物均为热爱中国文化的国际友人。" 
    with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    show beanbag with dissolve
    with Pause(1)

    hide beanbag with dissolve

    if persistent.game_completed:
        scene end menu with dissolve
    else: 
        scene bg shady with dissolve

    return

label start:
    play music "music/daily1.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『ゆるくいこうよ』")

    scene bg shady
    with fade
 
    """
    我讨厌学校的小卖部。
    
    不仅因为它卖袜子不卖短白袜，还因为它卖内裤不卖三角裤。发现这一点后，我只得悻悻地离开。

    最近不顺的事实在多得抱怨不完：
    """

    $ renpy.notify("💡Tip：“神粥”已添加至词典")
    $ unlock_tip("神粥")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“玫瑰战争”已添加至词典")
    $ unlock_tip("玫瑰战争")

    with Pause(0.5) 

    $ renpy.notify("💡Tip：“国补”已添加至词典")
    $ unlock_tip("国补")

    "牢神粥在经历“玫瑰战争”后就光荣退役了，在双十一先抬价再发券的“预热”下问新笔电when不如问国补when；"

    """
    被办公室“不懂事”的后辈拖下水无偿加班一小时就为了确定跟我八竿子打不着关系的奖学金候选人，最后发在朋友圈里的鸣谢名单里还没有我；

    班里评选奖学金只看综测不看绩点，凭什么绩点二点几的人都能拿而我不能拿啊——

    {clear}
    """

    $ renpy.notify("💡Tip：“现充”已添加至词典")
    $ unlock_tip("现充")

    """
    综测分这种东西完完全全就是现充分。
    
    对，现充分。
    
    作为高贵的拯救过世界的宅男，我光辉的履历三天三夜都写不完，才不稀罕这点分数。
    """

    $ renpy.notify("💡Tip：“负能量”已添加至词典")
    $ unlock_tip("负能量")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“史塔西虫洞”已添加至词典")
    $ unlock_tip("史塔西虫洞")

    "只要我愿意，把“负能量生成架”“基于史塔西虫洞的时间机器”报上去写几篇论文、申请几个专利不是随随便便拿国奖乃至诺奖！"

    $ renpy.notify("💡Tip：“地球OL”已添加至词典")
    $ unlock_tip("地球OL")

    "地球ＯＬ是最狗屎的游戏。"

    """
    所谓什么什么“团”、什么什么“协”、什么什么“会”，不过一套班子轮番唱戏。

    {clear}
    
    各种【加志愿时】【加文体分】的活动向来都是小团体特供。
    """

    $ renpy.notify("💡Tip：“BBS”已添加至词典")
    $ unlock_tip("BBS")

    "如果现实能像互联网那样尽可能公开透明就好了，毕竟只要一个ＢＢＳ就可以满足人基本的情报需求。"

    $ renpy.notify("💡Tip：“DQN”已添加至词典")
    $ unlock_tip("DQN")

    "可ＤＱＮ们有什么事只会重复“建小群－拉人－＠全体成员－扫邀请码－另建小群”的流程。"

    $ renpy.notify("💡Tip：“V信”已添加至词典")
    $ unlock_tip("V信")

    "V信一拉，满满当当的精神污染。"

    """
    {clear}

    在心里发了这么多牢骚，实际上我的脚才刚踏出小卖部的门。
    
    一阵凉风袭来，很舒服。
    
    嘛，从来没有什么不可战胜的夏天，１０月底的广东也是会入秋的。天是瓷色的，脏脏的但很耐看。
    
    我喜欢这样的天气，没那么耀眼和青春，超适合窝在家打游戏，出门也不是不可以接受。

    眼尖的我在人群中一眼就看见了林笃不知道为什么在小卖部门前的树下踢着石子。
    """

    window hide

    stop music fadeout 2.0

    show lindu unhappy at truecenter
    with dissolve 

    adv "人哪～果然还是多穿衣服比较好看！我默默地发出转凉后的第二声感慨。"

    $ renpy.notify("💡Tip：“galgame”已添加至词典")
    $ unlock_tip("galgame")
    
    adv "只要玩过galgame的都知道衣服有多重要。"

    $ renpy.notify("💡Tip：“HS”已添加至词典")
    $ unlock_tip("HS")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“薄纱”已添加至词典")
    $ unlock_tip("薄纱")
    
    adv "穿衣ＨＳ薄纱脱衣ＨＳ是业界显而易见的常识。"

    adv "以此类推，不脱丝袜也是黄油的好文明。"

    play music "music/woman.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：《善变的女人》")

    hide lindu unhappy
    with dissolve

    w "你在等谁吗？"

    r "没有。"

    w "感觉你不是很高兴？"

    r "胸中苦闷。"

    adv """
    林笃说出了像是恋爱中的少女会说的台词。

    ……不对，她就是！
    
    我赶紧开始想最近是不是亏待她了。
    
    每周的电话粥有好好煲，每月轮流请对方吃东西的约定也有好好执行……
    
    这个时候，就该求助galgame的经验了吧——
    
    galgame的经验galgame的经验galgame的经验……
    
    galgame只教我和女主表白后上垒……

    我迈步往前走去。
    
    林笃很自然地跟了过来，默默地。

    好吧，就来当一次她的垃圾桶。

    我抬头看向那瓷色的天空。
    
    只要她开心就是我开心。

    毕竟只有蓝天才最与她的笑容相称嘛。

    ……为了蓝色而清净的世界。
    """

    stop music fadeout 2.0

    scene black
    with fade
    with Pause(2)

    $ _game_menu_screen = None
    $ movie_length = 63
    $ skip_hide = 5.0
    if renpy.variant("pc"):
        $ movie_playing = "video/PC/op.webm"
    elif renpy.variant("mobile"):
        $ movie_playing = "video/Android/op.webm"
        
    call screen movie with dissolve

    $ _game_menu_screen = 'save'

label GUNDAM:
    scene bg shady
    with fade

    play music "music/play with.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『うまくいくかね？』")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“百do”已添加至词典")
    $ unlock_tip("百do")

    adv """
    百do说，首先要创造一个轻松的氛围。

    于是我拉开了外套的拉链，把双手背到脑后，走着自信的太空步，就像动画里的风流男主角一样——

    林笃莫名其妙地开始学起机器人走路。

    罢了，她要觉得这样比较轻松就好……
    
    对了，今天的林笃是少见的茉莉味。以前的林笃一般是柠檬味的……
    
    好，就以这个为切入点开启对话，而且要尽可能有趣：
    """

    w "……汝何故以茉莉味示人？"

    r "因为借的别人的洗发水。"

    adv "对话结束。宝可梦收服失败。"

    adv "不行，不能就这样放弃。"
    
    adv "我继续努力搜刮着脑子里的文言文："
    
    w "吾妈曾曰，倘能娶笃为妻，不离不弃，将于梦中笑醒也。"

    w "吾气而答曰，汝莫臀后生气哉！区区小笃，额……幼驯染耳！"

    adv "林怫然应曰："
    
    r "倭国画戏害人不浅，竟错把倭语当汉语。"

    w "汝之不慧，可与豚相比。此乃文化交融是也。"

    adv "笃怒目而视，似竖尾之犬。"

    window hide

    show lindu angry at truecenter
    with dissolve

    adv "我编不下去了。"
    
    w "好好好——坐下。"

    adv "林笃真的坐下了。"

    window hide
    show lindu doggy at truecenter
    with dissolve

    adv """
    对上她圆圆的眼睛，这就是传说中的犬系青梅么，好可爱……
    
    我的青梅不可能这么可爱。
    
    于是奖池还在叠加：
    """

    w "起立～乖，别苦闷了好不好？伸手……握手——"

    hide lindu doggy
    with dissolve

    scene shock
    with vpunch

    adv "吃了她一记头槌。茉莉味的。"

    scene bg shady
    with dissolve

    nvl clear

    "不知不觉走到了宿舍区。"

    $ renpy.notify("💡Tip：“MC”已添加至词典")
    $ unlock_tip("MC")

    "可能校方玩ＭＣ只会造火柴盒？"

    "四幢比麻将牌还方正的宿舍楼规整地占据着四个金角。"

    "刚有起色就回去便前功尽弃了。"
    
    "注意到门口停着私人单车，我灵机一动："

    scene bg bike
    with dissolve
    
    w "我们骑车去哪儿逛逛怎么样？"

    r "不想。"

    adv "精灵球又捉了个空。"

    w "为什么啊？"

    r "没有为什么。"

    adv "林笃作为女生，也有不好搞定的一面啊。"

    w "你刚才明明就盯着单车看了好久。"

    r "一般。"

    $ renpy.notify("💡Tip：“圆明新园”已添加至词典")
    $ unlock_tip("圆明新园")

    w "就去圆明新园怎么样？要是去太远我也骑不动呢。"

    r "都行。"

    w "那我现在去找共享单车～"

    r "不好。"

    adv "怎么又闹起别扭了！"

    adv "正当我深感像在带小孩子时，终于想起林笃穿的裙子不方便骑车！"

    $ renpy.notify("💡Tip：“安全裤”已添加至词典")
    $ unlock_tip("安全裤")

    adv"""
    为什么一开始发明来用于遮羞的内裤漏出来给别人看到又会衍生出另一种羞耻以至于要诞生安全裤这种东西照这样无限套娃下去是不是要在安全裤外再套一层安全裤的吐槽且放一边。
    
    （原来我在内心吐槽的语速可以这么快！）
    
    我自信满满地对症下药：
    """
    
    w "我载你去吧。"

    r "……"

    w "我想和你在一起的时间久一点嘛～"

    r "……"

    w "你不想和我在一起的时间久一点吗？"

    r "……"

    adv "我等待着她的回应。"

    r "……刚才胸口好痛。"

    adv "被脸红的她岔开了话题。"

    w "那一定是你很想很想和我去圆明新园，想到胸口痛吧。"

    r "那一定是我很想很想往你脸上喷防狼喷雾，想到胸口痛吧。"

    play music "music/obituary.mp3" fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：Obituary")

    w "走呗走呗走呗～"

    r "不跟大色狼走。"

    adv "我再也忍不住了，抓过林笃使劲挠她的胳肢窝。"
    
    w "故意的对不对～？"

    adv """
    或许我真的是大色狼。
    
    至少潜意识里是。
    
    但我当时真的没想过趁机吃豆腐。
    
    真的。
    """

    scene bg peach
    with dissolve
    
    adv "可大灰狼确确实实是不小心抓到小白兔了。"

    $ renpy.notify("💡Tip：“轻小说”已添加至词典")
    $ unlock_tip("轻小说")
    
    adv "我不想像某些轻小说男主一样，详细地描述是什么形状什么触感云云，唯一能透露的就是：比江恬那种一马平川的好一些些。"

    adv "……但也只是一些些而已。"

    r "嗤嗤嗤嗤……诶？快、快停手！我、我内衣歪……喂喂！哎——咕——嘿！"

    scene shock
    with vpunch
    
    adv "林笃扭过头来与我对视的那一瞬，她就像是预判了我的动作似的，巧妙地闪身把失去平衡的我摔在了地上。"

    scene bg bike
    with dissolve


    play music "music/sentence know.mp3" volume 0.75

    $ renpy.notify("🎵正在播放：『Sentence know』")

    adv "尝尽多重辛酸，克服无数苦难，抵达荆棘尽头，成就圆满夙愿……？"

    $ renpy.pause(2.0, hard=True)

    play music "music/wonderful time.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：《美好时光》")

    """
    {clear}

    骗你的。圆满不了一点。

    首先要解决林笃坐哪儿的问题。
    
    共享单车没有后座垫，于是只好委屈她扶住我的肩膀站着。
    
    她本人没有意见实在太好了。

    其次我是路痴。
    
    好在这是人手一部手机的２１世纪，再路痴都不至于迷路。只要林笃帮我看准路线就行。

    {clear}

    最后的问题还是出在我身上——
    
    哪有这么废的男朋友啊真是的，就连我都忍不住替林笃抱怨起来了——
    
    我压根都不知道一场“普通”的约会要做什么。
    
    只好启动我的色情回路了：

    {clear}

    全球实况直播把两人关进不达成一亿播放就不能离开的房间？
    
    孤男寡女共处一室，炒流量的最优解想都不用想……
    
    不不不，林笃一定会气得踢飞我，直到我的飞行速度超越宇宙第一速度化作夜空中最亮的星……

    医生游戏？
    """
    
    play music "music/obituary.mp3" fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：Obituary")

    r "医生，我胸口好痛～☆"
    
    w "好的，让我听听您心率是否正常。"
    
    w "麻烦解一下衣服，方便用听诊器。"
    
    r "【先谢|せんせい】Ｈ……"
    
    r "连着好几天我的胸口都闷闷的，今天更是痛得不行。听说您专治这个，我是托关系进来的。"
    
    w "我也是。"

    stop music fadeout 2.0
    
    """
    {clear}

    这是什么欧亨利式结尾吗……

    还是不整这种像创新作文命题的约会了，王道一点的就好吧。
    
    吃冰淇淋可丽饼鲷鱼烧大芭菲苹果糖章鱼烧汉堡肉蛋包饭这些galgame必吃榜上的东西就ＯＫ了。
    
    但是！
    
    没错，还有但是。

    {clear}
    
    就连目的地圆明新园，那儿是干什么的、进去要不要门票／预约、附近有什么，我都不知道。
    
    也就是一点功课都没做的状态。

    即便如此……！
    
    我还是把脚放上了自行车踏板。
    """

    r "欸欸欸欸！我还没有站稳啊——！"

    adv """
    看，我就说吧，自己在脑内妄想和吐槽的速度远高于现实时间的流速。

    这或许就是为什么魔法少女变身时反派从来不会发动攻击的解释。
    """

    scene bg gate
    with dissolve

    r "左转。"

    play music "music/kantai collection.mp3" fadein 1.0 volume 0.25

    $ renpy.notify("🎵正在播放：『みいろ』")

    w "是，提督！"

    adv "虽然我根本没玩过这游戏。"

    r "右舵！航向洞、九、洞！"

    adv "林笃松开一只手，威风凛凛地向东方指去。"

    w "右舵，航向洞、九、洞。到！"

    r "……可以开炮吗？"

    w "一切听提督的。"

    r "目标暨南大学，高爆弹，齐射，执行！"

    w "齐射射出！"

    play sound "boom.mp3" volume 1.5

    adv "我用力抓住握把，不，舵轮，拼命地摇。"

    r """
    噗哈哈哈！
    
    喔呼——把学校炸了……
    
    哎，嗨！
    """

    adv "林笃半站在后面，紧紧地搂住了我的脖子。"
    
    adv "我跟着她放声笑起来："

    play audio "boom.mp3" volume 1.5
    $ renpy.pause(0.5, hard=True)

    play audio "boom.mp3" volume 1.5
    $ renpy.pause(0.5, hard=True)

    play audio "boom.mp3" volume 1.5

    w """
    炸个稀巴烂吧！
    
    炸飞他们，统统！
    
    哈哈哈哈——
    """

    r "我俩好像反派喔。"

    w "哪天你当上了反派，别忘了叫上我一起。"
    
    w "我们一起‘地球侵略’！"

    $ renpy.notify("💡Tip：“大和号”已添加至词典")
    $ unlock_tip("大和号")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“波动炮”已添加至词典")
    $ unlock_tip("波动炮")

    w "不，不止，还要打造比大和号更大更宏伟的宇宙战舰，用波动炮干爆整个银河系哈哈哈哈哈哈!!!"

    play audio "boom.mp3" volume 1.5

    play audio "boom.mp3" volume 1.5

    play audio "boom.mp3" volume 1.5

    play audio "boom.mp3" volume 1.5

    play audio "boom.mp3" volume 1.5

    nvl clear

    "林笃笑得失声，她的裙子随风飘扬。"
    
    "笑完，她认真地说："
    
    r "即使我当了大ＢＯＳＳ你也会陪我吗？"

    w "我会追你到天涯海角。"

    $ renpy.notify("💡Tip：“光明顶”已添加至词典")
    $ unlock_tip("光明顶")
    
    w "把正派们在光明山顶都打得落花流水。"

    w "管它的正邪，到哪都陪着你。"

    r "许○……"

    stop music fadeout 5.0

    """
    {clear}

    这

    不

    是

    英

    雄

    的

    故

    事

    。

    {clear}

    从一开始就不是为了拯救世界放弃四大元老的身份，不是吗？

    从比一开始更远的开始就是想要与林笃共度的未来，不是吗？

    就在这时，我所钟爱的瓷色天空从远方飘来了绵绵的细雨。
    """

    window hide

    scene bg road
    with dissolve

    show rain

    play sound "<loop 0>rain.mp3" volume 1.0

    play music "music/sky.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『空を見上げて』")

    w "……你有带伞吗？"

    r "没。"

    w "我也没。"

    adv "九九八十一难之第四难。"

    r "既然如此，我们回去吧。"

    w "啊啊？可说好了要带你……"

    adv "我停住了脚，自行车也随之停下。"

    r """
    不用了。真的不用了。
    
    胸中已经不苦闷了。
    
    今天——我很开心。
    
    你呢？
    
    你开心吗？
    """

    adv """
    林笃对着回过头来的我露出一颗小小的虎牙。

    这是我今天见过最灿烂的笑容。

    我的答案毋庸置疑。
    """

    w "开心——！"

    scene bg bike back 
    with dissolve

    show rain

    """
    {clear}

    把爱船自沉铁底湾（其实是把共享单车跟它其他的小伙伴停一块儿）后，离回去还有段不短的距离。
    
    我担心地看了一眼林笃，她的衣服看起来也不是很厚的样子。
    
    林笃歪着脑袋不解地“嗯？”了一声。
    """

    w "我的帽子给你戴吧，头一定不能淋到雨。"

    r "那你怎么办？"

    w "我的外套有帽子的。"

    r "谢谢啦～我好喜欢你！"

    w "我也好稀饭你！"

    """
    {clear}

    林笃靠在我的肩上。我也自然地牵过她的手。

    当瓷色的天空降下雨幕，刷去脏的，秋是暖到雨打湿肩头也不觉得冷的，是窄到堪堪容两人于奶与蜜之间再无另者的。
    
    不用说，我们一定是世间最最最笨蛋的情侣，没有情人伞，没有雨后小故事，用脸接雨，用脚约会，徒见两人一块淋着雨慢慢往宿舍方向挪。
    
    心里既有反生出要是雨能一直下、路能一直往前延伸该多好的期望，也有宛若往一锅清水里下了一挂素面的自然。

    我相信我们都不会感冒。
    
    道理很简单，因为笨蛋是不会感冒的。
    """

    window hide
    $ quick_menu = False
    $ persistent.chapter_menu_active = True

    show chapter1 complete at truecenter 
    with dissolve
    $ renpy.pause(5.0, hard=True)

    hide chapter1 complete with dissolve
    with Pause(1)

    if persistent.game_completed:
        stop music fadeout 2.0
        stop sound

        $ quick_menu = True
    elif renpy.confirm("你现在可以通过标题界面的“开始游戏”按钮\n进入新的章节或者回顾已完成的章节。\n{size=-3}（按下“确认”继续下一章节，按下“取消”返回标题界面）{/size}"):
        stop music fadeout 2.0
        stop sound

        $ quick_menu = True   
    else:
        stop music fadeout 2.0
        stop sound
        
        scene bg shady 
        with dissolve
        $ renpy.pause(2.0, hard=True)
        
        $ quick_menu = True
        return


label FATE:

    scene bg classroom1
    with fade

    play music "music/daily2.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『どんぐりみいつけた』")

    R "哇呜～"
    
    adv "有人搓着手在我身旁坐下。"
    
    R "降温了呢。"

    adv "不用说，肯定是林笃。"
    
    adv "我维持着来时趴着的姿势，有气无力地指了指桌上那顶帮她占座的黑帽子，示意她帮我放回去。"

    r "我说啊，好歹打个招呼表示下欢迎吧。"
    
    adv "她边说着边小心地把帽子折起来塞进袋子里。"

    w "因为天冷了所以打不起精神啊。"

    r "天热了你也打不起精神不是么？"

    w "真不想被比我还晚到的家伙这样说。"

    """
    {clear}

    估计是觉得说什么都没用吧，林笃扶着额头轻轻地叹了口气。

    我和林笃学的东西天差地别，因此几乎没有机会挨到一块儿上课。
    
    通选课是例外，毕竟没什么门槛。
    
    就拿当下这节还差１min２２s就要开始上的……
    
    叫什么来着？反正是好长一串里带着“环境”的课来说，只上一学期，一学期三四次见面课＋若干慕课，结课交篇论文就行——用AI写咯。

    {clear}

    我算是看清楚了，这些人都是不睡午觉的怪物。
    
    下午的课，尤其是这种水课，后排的座位就像金子一样宝贵。
    
    考虑到不仅自己要坐，还得帮林笃占一个，于是我们只能次次坐前排。
    
    偏偏这个老师聒噪得不行，在他眼皮子底下讲几句话（咳咳，可能也不止几句话）就像犯了他命似的，搞得我跟林笃在这门破课上相当“出名”。
    
    好就好在这是大学不是高中，即使怪了点也没什么人舍得放下手机多搭理你一下……

    {clear}
    """

    adv "正当我在内心感慨时，忽而瞥到林笃这个季节还穿着裙子。"
    
    adv "我捶了一下她的大腿。"
    
    w "说降温了还穿裙子。"

    adv "林笃放下搓着的双手，不服气地说："
    
    r "也有女孩子这样穿啊。"

    adv "我环视了一圈才发现教室里大多女生都坚持穿着裙子来上课。真不容易。"

    r "虽然我也是刚到……"
    
    r "但其实你也是刚到吧？你头发还是乱的。"
    
    """
    {clear}

    她伸手就要来抓我不知哪儿翘起的头发。

    坐在前排干这种事有点害羞……
    
    被甩开后，林笃有点哀怨地看着我。

    哦对了，这是要汇报的另一件事：我开始留头发了。
    
    因、因为留头发可以少跑很多路省很多钱嘛！

    {clear}
    
    嗯……
    
    可能林笃想看也占一小部分原因吧，但只占一点点哦。
    
    在声明完绝对不能剪成微分碎盖、锅盖头如此种种现充发型后，头发就交给她吧，暂时就不自暴自弃地剃寸头了。
    """

    w "原来留头发是一件很麻烦的事。每次起床都要梳，梳了还要掉。起晚了来不及梳还不行。"

    r "我可不可以理解成，这是在想念我叫你起床去上学的日子？"
    
    adv "林笃一扫脸上的阴霾，笑嘻嘻地看着我。"

    w "敲门please！"

    r "不必多礼。"

    w "万一你下次进来时我在换衣服怎么办哪？"

    r "又不是没看过……"
    
    adv "林笃嘀咕道："
    
    r "而且也没什么好看的。"

    w "哈？你刚才说的话我都听到了。"

    r "噗噗！这个赘肉眼镜男超弱的www。"

    adv "受不了了，这个欠揍的青梅竹马似乎以为所有男的都有肌肉……！"

    w "你知道自己为什么怕冷吗？问题出在胸部，笨蛋！"

    r "……！"

    """
    {clear}

    毫不意外地打起来了。

    就在这时，老师终于来了，后面还跟着一个面目和善的大背头。
    
    不出所料，老师刚进门就狠狠瞪了我们一眼……今天也多谢关照。

    在那老登介绍这个大背头有多么多么厉害时，我才意识到平时他从来不会掐点到教室。
    
    稍微有点愧疚感。
    """

    stop music fadeout 2.0

    """
    {clear}
    
    照常识来说，这种请来的名校教授不是净吹嘘自己的资历就是长篇累牍地介绍自己的科研成果，更严谨地，后者也不过是前者的另一种表现形式。
    
    我很清楚，自己和林笃决不是那种歇斯底里地热心于地球环保事业的人，只是凑巧都有时间为了这两个学分而来罢了。

    觉醒完毕。看看手机沉沦会儿吧——
    
    嘿嘿，适当的娱乐也是必需的吧？绝对不是对这物欲横流的邪恶社会投降了喔？

    {clear}

    由于AI需求激增带来的硬盘内存大大大涨价仍在继续。
    """

    $ renpy.notify("💡Tip：“SSD”已添加至词典")
    $ unlock_tip("SSD")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“RAM”已添加至词典")
    $ unlock_tip("RAM")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“狗东”已添加至词典")
    $ unlock_tip("狗东")

    "我特意切到狗东看了一眼，一块１Ｔ的TLC颗粒SSD正向着千元大关突进，一条１６Ｇ DDR5的RAM就顶我３个月的工资。"

    play music "music/devil whisper.mp3" fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『Devil's whisper』")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“区块链”已添加至词典")
    $ unlock_tip("区块链")

    "昨天是区块链，今天是AI，首先遭遇冲击的永远是ToC。"

    "照这个趋势，要什么时候才适合买新电脑啊（趴）。"

    $ renpy.notify("💡Tip：“CloudFlare”已添加至词典")
    $ unlock_tip("CloudFlare")

    "昨天CloudFlare崩溃带着大大小小的网站一起瘫痪了。"

    """
    昨天完全没留意到……只顾着和林笃在电话里聊垃圾话然后睡觉。

    {clear}

    翻翻评论区看看——
    """

    RR "当初说是国产硬盘把价格打下来的怎么现在不吱声了？"

    RR "上半年真是好价了，据说到２７年都不一定能恢复。"

    RR "我说昨天怎么起飞不了。"

    $ renpy.notify("💡Tip：“⭐🦆🐜”已添加至词典")
    $ unlock_tip("⭐🦆🐜")

    RR "⭐🦆🐜了。"

    nvl clear

    RR "愿意信四大元老也是没谁了，只能说基本盘还是太牢固了🤣。"

    $ renpy.notify("💡Tip：“⏰”已添加至词典")
    $ unlock_tip("⏰")

    RR "这次CF崩溃是不是说明⏰的网络基建在世界都处于领先水平？"

    RR "好在我上半年装机入手了２根３２Ｇ的内存，现在一看赚死了。"

    RR "昨晚迫降的损失谁给我补啊。"

    $ renpy.notify("💡Tip：“航÷”已添加至词典")
    $ unlock_tip("航÷")

    RR "现在航÷认知都这么低下了吗？你知道CF对全球互联网的重要性吗就搁着论证赢学。"

    nvl clear

    $ renpy.notify("💡Tip：“神区”已添加至词典")
    $ unlock_tip("神区")

    RR "看这次一下炸出多少神区。"

    RR "外务省干活了？"

    RR "都别买，厂商看赚不到钱了自己就会降价。"

    RR "说得好我完全同意。"

    RR "你不要害我们装不了机。"

    $ renpy.notify("💡Tip：“85”已添加至词典")
    $ unlock_tip("85")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“十循永封”已添加至词典")
    $ unlock_tip("十循永封")

    RR "见证的是真烦……85呢谁at下？给楼上来个十循永封就老实了。"

    nvl clear

    RR "没用的。DIY圈寒冬这事上热搜了，什么牛鬼蛇神都来了。"

    $ renpy.notify("💡Tip：“串子”已添加至词典")
    $ unlock_tip("串子")

    RR "别理那人。纯串子引战来的，他小号被封好几个了都。"

    $ renpy.notify("💡Tip：“等等党”已添加至词典")
    $ unlock_tip("等等党")

    RR "唉，等等党输麻了。"

    """
    ……

    {clear}

    """

    stop music fadeout 2.0

    """
    在对应的帖子下回复水完经验，首页似乎就没什么吸引人的了。
    
    我看了眼时间，才过５min，所以我才说，那些屌毛啊，是把玻璃戳穿了才能玩足两节课吧？

    {clear}

    好无聊好无聊好无聊。
    
    我撑起下巴开始东张西望视奸别人在干什么。
    
    第一个就从身边的林笃下手……
    
    才怪。
    
    聪明人都是时刻留意监管者动向的，那种一看头脑就不是很好的求生者还是先撂一边吧。

    {clear}

    老登坐在我们斜前方的第一排。
    
    虽然用眼无法直接捕捉我们的动作，但这个距离恐怕出太大声也是会被他听到的。
    
    另外，什么嘛，他不也在低头看手机。

    买一送一，关顾下大背头的课堂吧。

    {clear}
    
    在我转向课件的那一瞬，大背头的眼神恰好与我对上，不超过一秒，我的眼睛迅速移开了——我还是不习惯直视别人的眼睛，这一点并没有随着和林笃交往有所改善。
    
    林笃倒是能很自然地看着对方的眼睛说话，有时甚至让我隐隐生出“会不会不太礼貌啊？”的担忧，不过一看到她和谁都能有说有笑便又觉得是自己多虑了。
    
    宇宙本不均衡、不对称，现充的世界就交给现充吧。
    """

    C "人类世正在两种未来间……"

    """
    {clear}

    出人意料地，大背头课讲得还不错，像是对这行真有热情在的。

    可惜零人在意……

    因为我把目光又重新放回到林笃身上了。
    
    她的手机立在一旁在刷这门课的慕课，她的小轻薄本不知道是什么时候搬了出来正在捣鼓什么报告，眼睛伸长一点还能看到Ａ面贴了一些可爱的熊猫贴纸。

    挨个儿审视了一遍手机安装的APP后，我决定读会儿轻小说——

    {clear}
    
    对啊，一开始我怎么就没想到，手机就该拿来读轻小说的，用电脑太浪费，平板设备我又没有。
    """

    $ renpy.notify("💡Tip：“笔电男大”已添加至词典")
    $ unlock_tip("笔电男大")

    """
    ↑ 笔电男大的丑态。

    ……

    看了一会儿眼睛就酸了。
    
    正好下课铃响了，还剩一节课。
    
    整体上，除了个别走动打水的，和上课时一片死寂的下面没什么两样。

    {clear}

    骚扰下林笃好了。
    
    两手在她的电脑屏幕前比了一只小狗。就像玩手影游戏那样。

    不理我。
    
    小狗的嘴巴动了起来：
    """

    scene bg classroom2
    with dissolve

    play music "music/wonderful time.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：《美好时光》")


    w "林笃先生哪，下课啦～您休息一下吧！"

    adv "屏幕上出现了一行字："

    r "没关系吗？"

    adv "我知道她在担心那个老登，干脆对着他的背影说了出来："

    w "下课了又管不着。"

    adv "“而且今天他也不上课”这句话我还是悄悄咽进了肚子。"
    
    adv "嘛，还是要对老师放尊重一点。"

    r "咦？下课了吗？"
    
    """
    {clear}

    林笃惊诧地把耳机摘下来。

    ……真会享受啊她。

    我点点头，然后深吸了一口气。
    
    因为降了温，教室从门到窗每条缝都堵得死死的，相当沉闷。
    """

    w "啊～好讨厌。"

    w "这两周的大好周末都被金工实习抽走了，下周四又要单独拿一个下午体测，我恨１１月。"

    adv "关于体测，由于金工实习的时间恰好与它冲突，学院专门又给我们安排到了下周四的下午。"

    adv "林笃很好奇："
    
    r "金工实习是干什么？玩黄金矿工？"

    adv "你怎么不说去德克萨斯当牛仔！"
    
    adv "我耐心地解释："
    
    w "是去造把锤子。"

    adv "结果很快就忍不住拿出上传学○通作业的照片吹嘘起来。"

    show hammer at truecenter
    with dissolve
    
    w "厉害吧？用什么锉刀啦车床啦刮啊削啊磨啊铣啊才造成这样一把小小的锤子的喔？"

    adv "但很快就被戳穿了。"
    
    adv "这个没良心的东西指着照片里我和别人造的并排放在一起的锤子哈哈大笑："
    
    r "没有对比就没有伤害。"

    hide hammer
    with dissolve

    """
    {clear}

    呣……！
    
    好吧，我承认这把锤子我自己造的成分不超过一半。
    
    全程实际上是我求同学求老师指导最后才笨手笨脚跌跌撞撞完成的。

    因为……我手就是很笨嘛。

    深深地、深深地叹气！
    """

    w "要是你在就好了。"

    window hide

    show lindu amazed at truecenter
    with dissolve

    r "哇呜～？今天意外地主动诶。"

    w "要是有你在，至少我四处求人也会更有动力一点。"

    adv "被半生不熟的人们嫌弃了好多次呢。"

    hide lindu amazed with dissolve

    r "我就知道。果然没有我就是不行呀～☆"

    w "对啊对啊！既然如此，就帮我把体测给测了吧！"

    r "驳回。"

    w "上诉！"

    r "维持原判。"

    """
    {clear}

    今天的暨南大学，依旧是瓷色的灰蒙蒙。

    上课铃响了，那位明明是在瑞士任教的大背头似乎很适应中国的教学（不过也是，他本就是中国人），很快又继续他激情的讲课。
    
    然而我们也丝毫没有停下这边的意思：
    """

    r "不过——"
    
    r "我可以过去给你加油！"
    
    adv "林笃说着比了个元气的胜利手势。"

    w "那算了。你千万别来。"

    r """
    欸——

    为什么为什么？
    
    不是说能给你动力嘛。

    我都测完咯，还怕跑不过我啊？
    """

    adv """

    不用怕，就是跑不过。
    
    什么女超人５０米能跑７秒多啊！
    
    明明我觉得８秒就已经很快了说。
    """

    w "……我跑５０米一定会摔倒的。"

    r "那不就很需要人看了嘛。"

    w "……１０００米也一定会跑断腿的。"

    r "那不就更需要人扶了嘛。"

    w "我发现你还真是犟欸。"

    r "‘生活就像海洋，只有意志坚强的人才能到达彼岸’！"

    """
    {clear}

    这是在燃什么啊……

    说到犟，我就想起上次因为上上次下雨没去成而补偿的约会。
    
    当时在餐厅吃完饭，林笃坚持要把柠檬茶里最后一片柠檬吃完再走，即使我大方一回告诉她如果想的话可以再买，结果被她一口回绝还言之凿凿不要浪费……
    """

    $ renpy.notify("💡Tip：“人人点评”已添加至词典")
    $ unlock_tip("人人点评")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“米团”已添加至词典")
    $ unlock_tip("米团")

    "顺带一提，点餐是在她指导下跟她分头在人人点评和米团找对应的代金券和团购对比出的最优解，匪夷所思的是最后居然还被她神经大条地教育一顿“跟别的女孩子出门吃饭不要这样子喔”……"

    r "好吧好吧，你要不乐意就算了。才不强求呢。"

    stop music fadeout 2.0
    
    """
    {clear}

    林笃撅起了嘴。

    这句话终于把我拉回了思绪。

    无视掉老登回头的警告，我深感都是自找的：
    
    也是这句话，稍稍地让我感到有点寂寞。
    """

    scene bg gym
    with fade

    play music "<from 20>music/never give up.mp3" fadein 3.0 fadeout 1.0 volume 0.25

    $ renpy.notify("🎵正在播放：『负けないで』")


    """
    {clear}

    2025年１１月２７日下午。
    
    体测。
    
    平生大敌。

    已知你是一个立定跳远和引体向上都是０分的废物——我就是立定跳远连自己的身高都跳不到、引体向上也一个都拉不起来怎么啦＞＜——
    
    要如何抵达幸福的６０分及格线？

    ——我也不对自己的卑劣遮遮掩掩了，答案就是靠一点小巧思。

    {clear}

    测身高体重时尽可能空腹、脱外套、抬头挺胸，如果身体比较极限的话就再考虑微微地踮下脚，只要不被当面指出就是本事（抬头挺胸）。
    
    对于我的话，这一关相当于是白送的必须拿下。
    
    其实ＢＭＩ这一块我不用这些小手腕也能满分，嘻嘻嘻。

    {clear}

    来到坐位体前屈。
    
    秘诀也差不多，腿可以微微抬一点嘛，反正又看不到！
    
    狠一点的话不要推要用砸！
    
    用你的气势向那块板子砸去！
    
    长腿叔叔可能确实拿它没什么脾气，但我的话，２５cm的满分也很容易啦，嘻嘻嘻。

    {clear}

    ……肺活量好像没什么好方法，如果有什么小妙招请联系我，拜托了。

    在尝试了不下六次的肺活量测试终于吹到３３００整得学生义工都把我给看面熟了后，我踏上了操场赛道。
    """

    scene bg playground
    with dissolve

    nvl clear

    "该死。今天的风又大又冻人。"
    
    "我一听到运动场的哨声还肚子痛。"

    play music "music/to the beginning.mp3"fadeout 1.0 volume 0.3

    $ renpy.notify("🎵正在播放：『To the beginning』")


    """
    这是一场孤身一人的战斗……

    你以为我在为谁而战斗……

    我问你：你在为谁而战？

    你有属于自己的「意志」吗？
    """

    stop music fadeout 1.0

    $ renpy.notify("💡Tip：“中二”已添加至词典")
    $ unlock_tip("中二")

    with Pause(0.5)

    $ renpy.notify("💡Tip：“尴尬癌”已添加至词典")
    $ unlock_tip("尴尬癌")

    """
    {clear}

    好吧以上都是我瞎编的求你别再往下看了怎么会这么中二我自己看得尴尬癌都犯了啊啊啊啊啊啊啊啊啊啊。
    
    不用说，先跑五十米再跑一千米。
    
    五十米重在抢跑，一千米注意化曲为直——
    
    但一定不要不要不要太明显。
    """

    $ renpy.notify("💡Tip：“Docker”已添加至词典")
    $ unlock_tip("Docker")

    """
    就像程序员不仅要在自己的环境下跑通程序，在其他运行环境下也得保证其正常运行一样——希望地球ＯＬ尽早实装Docker——
    
    站上五十米赛道预测试一下起跑：口令喊完“预备”后大约是按照我的语速从１数到３，“跑”喊出来。

    {clear}
    
    既然如此，我就在２.５处开润。
    
    大约我跑出两三步那些现充们才会开始行动。

    这就是先手。

    只要时间卡得够准，裁判就会本着“多一事少一事”的原则，不会把我召回。

    跑进８秒，YES！

    {clear}
    """
    
    adv """
    到我了。

    深吸一口气。

    准备好起跑姿势。
    """

    R "各就各位——"

    adv "压低身姿。"

    R "预备——"

    adv """

    把身体重心逐渐转移到右脚。
    
    与此同时开始数数：

    一……

    二……

    二点五……

    就是现在！

    我的左脚跨了出去，右脚随后跟上，两条决算不上健壮的手臂用力摆起来。

    三！
    """
    
    play music "music/wall.mp3" fadein 2.0 fadeout 1.0 volume 0.75

    $ renpy.notify("🎵正在播放：『越えられない壁』")

    """
    {clear}
    
    身后传来了“啧”的不屑声。
    
    我会在内心“啧”回去的。

    我当然知道，自己的小人行为势必会被那群体育现充哥所不齿。

    但我要说，真是一群头脑简单四肢发达的家伙。

    他们可从来没想过，生来与运动无缘的家伙要怎么过体测。

    {clear}
    
    这不是他们关心的。

    因为那些人从来就不和他们生活在一个世界。

    就算知道了又能怎样？

    看我暂时领先在你们前面就这么不爽吗？

    只是拼尽全力想要一个“通过”的结果而已。

    为此不得不拾起讨厌的体育，疯狂耍着小聪明把体测测成了什么下三滥智斗。

    {clear}

    我讨厌体育、我讨厌拍照、我讨厌集体活动。

    我讨厌他们。

    头脑简单、四肢发达。

    ……看到一对狗男女有说有笑地走过。

    ……不知道林笃这个时候在干嘛呢？

    如果她知道我此时正一如之前咬牙切齿地诅咒着现充会怎么想呢？

    {clear}

    她每次听到这种话也从来没有当面指责过我。

    只是寂寞地笑……

    真奇怪。
    
    按照划分标准，毫无疑问我在连着她一起骂的。

    我没有骂她的意思。不如说，怎么舍得骂。

    但事实就是，在没有特别声明的情况下，把她连坐了。

    {clear}

    可她也不生气。

    为什么？

    我的眼角不自觉地寻找起她的身影。

    怎么可能呢。

    我已经把她赶走了。就在上周下午的水课。

    我的心隐隐地传来一阵绞痛。

    {clear}

    为什么、为什么会这么痛呢？

    就像要把整个心脏都撕裂一样、就像要把整个人都撕裂一样……

    的绞痛。

    我分不清：

    究竟是肌肉适应不了一时的剧烈运动导致的，还是牵挂林笃的心太痛导致的。

    逼近终点，在压低重心前屈冲刺时，一阵痉挛袭来。

    {clear}

    轰然倒塌在最后的终点线。
    
    终究还是过了。真讽刺。

    当然不会有人来扶。

    因为我先赶走了自己的青梅竹马，再亵渎体育精神背叛了在场的所有人。

    现充们嘲笑我都来不及。

    我想，这就是报应。

    {clear}

    大概是还带着最后一点的期待吧，我刻意放慢了爬起的动作——
    
    怎么可能会有人来扶呢？
    
    看了一眼成绩，确实进了八秒。
    
    目的已经达成了。除了收场不太优雅外没什么可挑剔的。
    
    此时我总算意识到了来自身边人投来的诧异目光，低头一看自己的白衬衫，不赖，对操场红漆地面的完美篆刻。
    """

    show shirt at truecenter
    with dissolve

    adv "先、先回宿舍换件衣服再来接着跑一千米吧。我走向操场的出口。"

    hide shirt
    with dissolve

    adv """

    所有思考像蒙上了一层雾而变得脆弱而不理智。

    好像摔坏了。

    我悠悠的心。
    """

    scene bg stairs
    with dissolve

    adv """
    拐过前面的树篱，就可以看到来时走下的阶梯了。

    快走吧，别丢人现眼了。

    快离开吧，这里本就容不下你。

    即便如此……为了那可笑的自尊……

    一手护住自己胸前那片火红，一手还在装作正常摆臂行走的我真是傻瓜。

    落单的傻瓜。

    有风就有虫鸣、草动和水滴，窸窸窣窣，沙沙作响。

    接二连三地打着喷嚏，口袋里又没有纸。

    只能任由手的黏糊糊，带着满是尘土的脸更加狼狈。

    不要看我……！

    远方刺耳的口哨声和脚板摩擦地面的声音，那么凌乱又那么飘渺。
    """

    play music "<from 1>music/spring.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：《春》")


    adv "直到我看见——"

    r "这里——！"

    adv """
    林笃。
    
    那个现充。
    
    那个这么冷的天还穿着裙子挨冻的傻瓜。
    
    就站在阶梯那儿向我使劲地挥着手。

    我到底哪里好了。

    值得你为我做这么多吗？

    我不明白啊……

    我会厚颜无耻地把这一切当作理所当然的……

    因为我就是这么卑劣的人物啊……

    眼里的景色变得模糊起来。

    仿佛只剩下了站在阶梯那儿的她。

    那些不要紧的东西变模糊就变模糊了吧。

    我向前踉跄着走去。

    一步……

    两步……

    阶梯也向着我走来。

    二点五步……

    三步……

    一定要向她说“对不起”而不是“不好意思”。
    
    我的脑子迷迷糊糊地这样想。
    """

    w "林笃——！"

    nvl clear

    "登上这段阶梯。"

    "我走完了最后这段孤身一人的５０米。"


    window hide
    $ quick_menu = False
    $ persistent.music_room_active = True

    show chapter2 complete at truecenter
    with dissolve
    $ renpy.pause(5.0, hard=True)

    hide chapter2 complete with dissolve
    with Pause(1)

    if persistent.game_completed:
        stop music fadeout 2.0
        stop sound

        $ quick_menu = True
    elif renpy.confirm("你现在可以通过标题界面的“鉴赏”按钮\n回顾已收集的歌曲。\n{size=-3}（按下“确认”继续下一章节，按下“取消”返回标题界面）{/size}"):
        stop music fadeout 2.0
        stop sound 
        
        $ quick_menu = True  
    else:
        stop music fadeout 2.0
        stop sound

        scene bg shady 
        with dissolve
        $ renpy.pause(2.0, hard=True)
        $ quick_menu = True 
        return

label HACKER:
    play music "music/a little happiness.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『A little happiness』")

    scene bg dorm
    with fade

    nvl clear

    """
    我想说说关于女儿的两件事。

    有关女儿的名字就隐去了，用大家都熟悉的“江恬”来称呼吧。

    第一件事发生在江恬上幼儿园的时候。
    
    她回到家一副闷闷不乐的样子。我赶忙问发生什么了。

    林笃先生代替不高兴的女儿回答道：
    """
    
    r "幼儿园课上教剪纸，其他小朋友剪出了小狗、小马、小羊，但小恬似乎就……不太在行。"

    adv "江恬沉默着从她的小书包里拿出一份皱巴巴的剪纸。"

    adv "我努力安慰着江恬："
    
    w """
    小甜甜别伤心啦～爸爸还是能看出你在剪什么的对不对？
    
    这次剪得不好多练习就好啦……你看，这只袋鼠不是挺可爱的嘛～
    
    有一个口袋，你还给它戴上了一副拳击手套。多棒的创意啊——
    """

    j "……那是熊猫正在吃的竹子。"
    
    adv "江恬打断了我。"

    w "啊？呵呵呵，呃嗯……"
    
    adv "暂且不管旁边一脸幸福的林笃，我搬出笔记本电脑："
    
    w "那爸爸和你一起来学剪纸吧！"

    adv "……"

    $ renpy.notify("💡Tip：“领域展开”已添加至词典")
    $ unlock_tip("领域展开")

    w "相信爸爸，这次一定……领域展开！"

    adv "二维的剪纸在我手间展开，出现的，是浩瀚的银河系……"

    r "破——！"
    
    adv "随着林笃强忍住笑意的宣告，银河系一瞬间坍塌成两段碎纸。"

    j "爸爸已经很努力了。"
    
    adv "小不点充满慈爱和宠溺（？）地摸了摸我的头。"

    w "不行不行不行！我要再试一次！"

    j "爸爸，这已经是第八张纸了。"

    w "小甜甜你知道吗？爱迪生发明灯泡可是经历了1600多次失败喔？"

    adv "江恬低头看向她第三次尝试就已经剪好的小熊猫（送给她妈妈的）。"
    
    j "爸爸，真是废废的呢。"

    adv "林笃鹦鹉学舌道："
    
    r "爸爸，真是废废的呢。"

    adv """
    往好的方面想，至少我动手能力差、不擅长做手工这一点传到江恬这一代已经好了不少不是吗？
    
    这么想或许可以好受一点……
    
    怎么可能能够接受啊！
    
    按融合遗传的观点来说，不就是林笃把她的正属性给了江恬，但即便如此还是抵消不了我的红词条么！

    我放弃了剪纸，去网络世界逃避现实了。

    ……
    
    当我回过神来，才发现江恬就趴在我身边盯着电脑屏幕看。

    我摸了摸她的头。
    """
    
    w "你在这儿看了多久啦？"

    j "嗯……"
    
    adv "江恬想了一会儿。"
    
    j "也没看多久吧？从爸爸自闭那会儿开始的。"

    adv "我切到桌面看了眼右下角的系统时间，这不是过去了一个钟头吗！"

    adv "幼儿园小孩居然能对着这么枯燥的内容看那么久……我不由得佩服起这位种子选手。"

    j "爸爸，这个是什么？"
    
    adv "她的手指指着一个图标。"

    $ renpy.notify("💡Tip：“洋葱路由”已添加至词典")
    $ unlock_tip("洋葱路由")

    w "Tor浏览器，与一般的浏览器不太一样，采用洋葱路由流量的方式进行加密连接，配合俄罗斯的SMS-Activate可以实现几乎完全匿名的上网噢。"

    j "那这两个开着的页面是？"
    
    adv "江恬歪着头。"

    $ renpy.notify("💡Tip：“渗透测试”已添加至词典")
    $ unlock_tip("渗透测试")

    w "蚁剑和冰蝎。用来做渗透测试……"

    adv "那一晚，江恬在书房听我讲了很久。"

    stop music fadeout 2.0

label ADULT:
    nvl clear

    stop music fadeout 2.0 # 如果是从章节选择页面直接进来，就把标题界面音乐暂停掉

    scene bg dorm
    with fade

    """
    我跟林笃曾讨论过江恬的事，甚至于一路谈到了该怎么给江恬做性教育。
    
    清楚地记得，当时林笃的脸唰地一下红透了。

    场面一度陷入了尴尬。
    
    我决定活跃下气氛，从床上爬起来：
    """

    play music "music/happiness is everywhere.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『Happiness is everywhere』")


    w "其实就一句话——你妈不是处女！"

    r "谁他妈是处女！"
    
    adv "林笃坐了起来，飞快地接上了吐槽。"

    w "噢，原来你他妈不是处女啊？"
    
    adv "使了一下坏。"

    r "嘶……我、我他妈当然是处女！"

    w "你妈是处女的话你是从石头蹦出来的吗？"

    r "我、我……操你妈!!!"

    window hide

    show lindu shy at truecenter
    with dissolve

    w "美少女的包袱呢？"

    adv "只见林笃边揉太阳穴边吟诵："
    
    r "‘林笃终得自由……属于她的故事全貌也终将得以展现……’"

    adv "对不起我开玩笑的不会有下次了再也不敢了。"

    adv "我笑着扣上她的五指轻轻地说。"
    
    w "不过说真的：你也快不是了。"

    scene bg family 
    with dissolve

    adv "林笃害羞地抓起一个枕头就朝我扔了过来。"

    hide lindu shy with dissolve

    adv """

    ……

    时光荏苒，到了江恬上小学的时候，就差不多该由林笃给她做这方面的教育了。

    看着女儿一天天长高，我心里满是感慨。

    但与此同时我也感到十二万分的悲痛！

    是悲痛啊！这种心情你懂吗？

    帮女儿洗澡时听她信誓旦旦地宣称“长大要跟爸爸结婚”的事恍若昨天，那个喊着“爸爸的胡子好扎”又超级黏爸爸、和爸爸的感情好到连妈妈都要嫉妒的小不点，居然有一天也要登上通往成人的阶梯……
    
    被别家的土猪拱白菜什么的……

    趁我一人坐在客厅无声地哭泣时，林笃已经拉着江恬进了房间开小会。

    林笃在这方面一直很害羞……大丈夫？

    我承认自己干了件不太光明的事：把耳朵贴在门板上偷听。
    
    会找个机会补偿她们的。
    """

    play music "music/kotatsu.mp3" fadein 1.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：『KOTATSU!!』")


    r """
    小恬啊，你听好喔……
    
    你以后一定会遇见这样的人——可能稍微有点帅气，又或者可能稍微有点不起眼。
    
    但不管怎么样，他对你一定是‘特别’的，足以让你在心中悄悄抱有和别人‘不一样’的感觉。
    
    在爸爸妈妈老了力所不及的地方，在你感到寂寞的时候，照顾你、陪伴你走完剩下的路……
    """

    j "妈妈才不会老～"

    adv "林笃没有管撒娇的江恬，坚持认真地说下去："
    
    r """
    会有那么一天的。而且妈妈和爸爸打心底盼望着那一天早些到来。
    
    那一天小恬要穿着最漂亮的衣服带着最灿烂的笑容跟我们告别喔？
    
    你也终于有机会组建自己小小的家庭，在城市小小的一隅安放自己小小的幸福。
    
    小小的幸福通过骨肉的纽带相连。
    
    再像蒲公英一样散落各地，开花结果，如此传承。
    
    汇聚起来，才是‘家族’。
    """

    j "就和爸爸妈妈一样吗？"

    r """
    嗯。但爸爸妈妈是从小就认识的青梅竹马，每个女孩子的那个他都是不一样的，这取决于你的‘抉择’。
    
    不要妄自菲薄，大胆地、自由地去爱，和喜欢的人结合是一件非常、非常幸福的事……
    
    但在作出‘抉择’时一定要慎重，不能意气用事。
    
    不管长到多大，哪怕变成老太太，也不要因未作出的‘抉择’而遗憾、而悔恨。
    
    相信幸福就在身边，沿着你做出的‘抉择’幸福地走下去。
    
    你做出什么‘抉择’爸爸妈妈都会和你站在一起……
    """

    adv "我悄悄松口气，放下心来。"

    adv "今天的晚饭，就由我来做吧。"

    window hide
    $ quick_menu = False
    $ persistent.final_unlocked = True

    show chapter3 complete at truecenter
    with dissolve
    $ renpy.pause(5.0, hard=True)

    hide chapter3 complete with dissolve
    with Pause(1)

    if persistent.game_completed:
        stop music fadeout 2.0
        stop sound

        $ quick_menu = True
    elif renpy.confirm("最终章已解锁。在此之前的一个小小提示：\n在你所不留意的角落或许藏着什么。\n{size=-3}（按下“确认”继续下一章节，按下“取消”返回标题界面）{/size}"):
        stop music fadeout 2.0
        stop sound
        
        $ quick_menu = True     
    else:
        stop music fadeout 2.0
        stop sound

        scene bg shady 
        with dissolve
        $ renpy.pause(2.0, hard=True)
        $ quick_menu = True 
        return

label SEX:
    scene bg r18 
    with fade

    play music "music/winter.mp3" fadein 2.0 fadeout 2.0 volume 0.75

    $ renpy.notify("🎵正在播放：《冬》")

    r "简直是虐待……我说啊……呜，第一次就尝试这种姿势真的没关系么？"

    w "我也很紧张啊……但不是你说的‘太害羞了，没办法直视你的脸’嘛。"

    nvl clear

    scene bg hometown
    with dissolve

    """
    嗯。这次没有任何的假药。

    我们就是在偷偷干你以为的那种事。

    事情要从大四上学期的寒假我跟林笃回老家过年说起。
    
    彼时我们的关系已经是人尽皆知的地步。回去也有向老家的奶奶和林笃家那边的爷爷奶奶报个到的意思。

    该怎么说呢……果然还是非常不习惯应付不太熟的七大姑八大姨，更别提林笃家的。

    加上老家那种乡下地方网络也不是很好，待了个三四天我就想回深圳了。

    {clear}

    于是我非常无耻地向林笃提议“要不我们先回去？”

    一拍即合——她的理由是“我实在不想再来来回回吃那几道年夜菜啦！”

    对不起爸爸妈妈叔叔阿姨还有许家林家的列祖列宗。

    顶着亲戚们“这么急着带自己的小女朋友走啊？”的调侃，我就带着林笃先一步于爸爸妈妈跟叔叔阿姨下深了。

    我不会说家乡话，待在那儿总像个局外人。

    尽管户口把我锚定，但我确信自己悠悠的心——她的归属之地不在那儿。

    {clear}

    那么在哪儿呢？

    深圳应该是首选的排除项……

    深圳的节奏总是令人窒息。

    但那是我从小所居住的城市，更是与林笃一切的起点。

    就算这份记忆是因欧泊瑟弗妖观测而起世界重构的结果，我也不在乎。

    {clear}

    不如说，你敢保证昨天的你100%%就是你而不是别人灌到脑里的记忆正在囚禁甚至重塑着你吗？

    即便按下“以今日之我攻昨日之我”的思想革新不表，要知道，我们全身上下的所有细胞每隔七年就会完成一次新陈代谢。

    这意味什么？只消七年，弹指一瞬，我将无我，你将无你。

    承认吧，街头所攒动的熙熙攘攘，那一颗颗沾沾自喜的人头，不过一艘艘坚信自己永不沉没的忒修斯之船。仅此而已。

    睁开眼所迎接的，不仅是新的一天，还有新的自己。

    {clear}

    所以——要问我【新|心】的归属地：

    那不是任何一个具体的地名。
    
    而是、想必是，与林笃在一起的每一处。

    跟随启明的新星，前往我们的约定之地——

    我如此坚信：

    我们终将抵达那淌着奶与蜜之地，与那并不遥远而显得伸手可及的未来。

    """

    window hide
    $ quick_menu = False

    show fin at truecenter 
    with dissolve

    stop music fadeout 5.0

    $ renpy.pause(5.0, hard=True)

    scene black
    with fade
    with Pause(2)

    $ _game_menu_screen = None
    $ movie_length = 117
    $ skip_hide = 5.0

    if renpy.variant("pc"):
        $ movie_playing = "video/PC/L_ed.webm"
    elif renpy.variant("mobile"):
        $ movie_playing = "video/Android/L_ed.webm"

    call screen movie with dissolve

    $ _game_menu_screen = 'save'
    $ persistent.game_completed = True
    $ quick_menu = True 

    # 解锁ed
    play music "music/ed.mp3" volume 0
    stop music
    stop sound

    scene end menu 
    with fade

    return
