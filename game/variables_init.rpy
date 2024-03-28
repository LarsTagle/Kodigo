define mcname = Character("[mc]")
define loc = Character("[place]")
define n = Character("Narrator")
define mom = Character("Mommy Sheilly")
define greg = Character("Gregory")
define emil = Character("Emil")
define carlos = Character("Carlos")
define madam = Character("Madam Alexandra")
define aling = Character("Aling Erin")
define lurs = Character("Johnny")
define j = Character("Mr. Jay")
define crush = Character("Sofia")
define mark = Character("Kuya Mark")
define mike = Character("Mike")
define mich = Character("Madam Michelle")
define guard = Character("Manong Guard")
define dev = Character("Mr. Devier")
define points = 0
define emil_decision = ""
define madam_decision = ""
define johnny_decision = ""
default persistent.gender = ""

# NVL Characters are used for the phone texting
define mc_nvl = Character("[mc]", kind=nvl, image="mc", callback=Phone_SendSound)
define g_nvl = Character("Gregory", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#image definitions, we can minimize this to a for loop latur
image mc angry_casual = "images/Characters/[persistent.gender] angry_casual.png"
image mc blushed_casual = "images/Characters/[persistent.gender] blushed_casual.png"
image mc confused_casual = "images/Characters/[persistent.gender] confused_casual.png"
image mc happy_casual = "images/Characters/[persistent.gender] happy_casual.png"
image mc neutral_casual = "images/Characters/[persistent.gender] neutral_casual.png"
image mc sad_casual = "images/Characters/[persistent.gender] sad_casual.png"
image mc shocked_casual = "images/Characters/[persistent.gender] shocked_casual.png"
image mc sleepy_casual = "images/Characters/[persistent.gender] sleepy_casual.png"
image mc angry_uniform = "images/Characters/[persistent.gender] angry_uniform.png"
image mc blushed_uniform = "images/Characters/[persistent.gender] blushed_uniform.png"
image mc confused_uniform = "images/Characters/[persistent.gender] confused_uniform.png"
image mc happy_uniform = "images/Characters/[persistent.gender] happy_uniform.png"
image mc neutral_uniform = "images/Characters/[persistent.gender] neutral_uniform.png"
image mc sad_uniform = "images/Characters/[persistent.gender] sad_uniform.png"
image mc shocked_uniform = "images/Characters/[persistent.gender] shocked_uniform.png"
image mc sleepy_uniform = "images/Characters/[persistent.gender] sleepy_uniform.png"

image friend_1 angry_casual = "images/Characters/[friend_1] angry_casual.png"
image friend_1 blushed_casual = "images/Characters/[friend_1] blushed_casual.png"
image friend_1 confused_casual = "images/Characters/[friend_1] confused_casual.png"
image friend_1 happy_casual = "images/Characters/[friend_1] happy_casual.png"
image friend_1 neutral_casual = "images/Characters/[friend_1] neutral_casual.png"
image friend_1 sad_casual = "images/Characters/[friend_1] sad_casual.png"
image friend_1 shocked_casual = "images/Characters/[friend_1] shocked_casual.png"
image friend_1 sleepy_casual = "images/Characters/[friend_1] sleepy_casual.png"
image friend_1 angry_uniform = "images/Characters/[friend_1] angry_uniform.png"
image friend_1 blushed_uniform = "images/Characters/[friend_1] blushed_uniform.png"
image friend_1 confused_uniform = "images/Characters/[friend_1] confused_uniform.png"
image friend_1 happy_uniform = "images/Characters/[friend_1] happy_uniform.png"
image friend_1 neutral_uniform = "images/Characters/[friend_1] neutral_uniform.png"
image friend_1 sad_uniform = "images/Characters/[friend_1] sad_uniform.png"
image friend_1 shocked_uniform = "images/Characters/[friend_1] shocked_uniform.png"
image friend_1 sleepy_uniform = "images/Characters/[friend_1] sleepy_uniform.png"

image friend_2 admiring_casual = "images/Characters/[friend_2] admiring_casual.png"
image friend_2 angry_casual = "images/Characters/[friend_2] angry_casual.png"
image friend_2 blushed_casual = "images/Characters/[friend_2] blushed_casual.png"
image friend_2 confused_casual = "images/Characters/[friend_2] confused_casual.png"
image friend_2 happy_casual = "images/Characters/[friend_2] happy_casual.png"
image friend_2 neutral_casual = "images/Characters/[friend_2] neutral_casual.png"
image friend_2 sad_casual = "images/Characters/[friend_2] sad_casual.png"
image friend_2 shocked_casual = "images/Characters/[friend_2] shocked_casual.png"
image friend_2 sleepy_casual = "images/Characters/[friend_2] sleepy_casual.png"
image friend_2 admiring_uniform = "images/Characters/[friend_2] admiring_uniform.png"
image friend_2 angry_uniform = "images/Characters/[friend_2] angry_uniform.png"
image friend_2 blushed_uniform = "images/Characters/[friend_2] blushed_uniform.png"
image friend_2 confused_uniform = "images/Characters/[friend_2] confused_uniform.png"
image friend_2 happy_uniform = "images/Characters/[friend_2] happy_uniform.png"
image friend_2 neutral_uniform = "images/Characters/[friend_2] neutral_uniform.png"
image friend_2 sad_uniform = "images/Characters/[friend_2] sad_uniform.png"
image friend_2 shocked_uniform = "images/Characters/[friend_2] shocked_uniform.png"
image friend_2 sleepy_uniform = "images/Characters/[friend_2] sleepy_uniform.png"
