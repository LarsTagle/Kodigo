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
define mark = Character("Kuya Mark")
define mike = Character("Mike")
define mich = Character("Madam Michelle")
define guard = Character("Manong Guard")
define dev = Character("Mr. Devier")
define points = 0
define emil_decision = ""
define madam_decision = ""
define johnny_decision = ""

#for quiz
default persistent.gender = ""
image mc_happy = "images/Characters/[persistent.gender] happy_uniform.png"
image mc_sad = "images/Characters/[persistent.gender] sad_uniform.png"

# NVL Characters are used for the phone texting
define mc_nvl = Character("[mc]", kind=nvl, image="mc", callback=Phone_SendSound)
define g_nvl = Character("Gregory", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#image definitions, we can minimize this to a for loop latur
image mc angry_casual = "images/Characters/[current_gender] angry_casual.png"
image mc blushed_casual = "images/Characters/[current_gender] blushed_casual.png"
image mc confused_casual = "images/Characters/[current_gender] confused_casual.png"
image mc happy_casual = "images/Characters/[current_gender] happy_casual.png"
image mc neutral_casual = "images/Characters/[current_gender] neutral_casual.png"
image mc sad_casual = "images/Characters/[current_gender] sad_casual.png"
image mc shocked_casual = "images/Characters/[current_gender] shocked_casual.png"
image mc sleepy_casual = "images/Characters/[current_gender] sleepy_casual.png"
image mc angry_uniform = "images/Characters/[current_gender] angry_uniform.png"
image mc blushed_uniform = "images/Characters/[current_gender] blushed_uniform.png"
image mc confused_uniform = "images/Characters/[current_gender] confused_uniform.png"
image mc happy_uniform = "images/Characters/[current_gender] happy_uniform.png"
image mc neutral_uniform = "images/Characters/[current_gender] neutral_uniform.png"
image mc sad_uniform = "images/Characters/[current_gender] sad_uniform.png"
image mc shocked_uniform = "images/Characters/[current_gender] shocked_uniform.png"
image mc sleepy_uniform = "images/Characters/[current_gender] sleepy_uniform.png"

image roommate angry_casual = "images/Characters/[roommate] angry_casual.png"
image roommate blushed_casual = "images/Characters/[roommate] blushed_casual.png"
image roommate confused_casual = "images/Characters/[roommate] confused_casual.png"
image roommate happy_casual = "images/Characters/[roommate] happy_casual.png"
image roommate neutral_casual = "images/Characters/[roommate] neutral_casual.png"
image roommate sad_casual = "images/Characters/[roommate] sad_casual.png"
image roommate shocked_casual = "images/Characters/[roommate] shocked_casual.png"
image roommate sleepy_casual = "images/Characters/[roommate] sleepy_casual.png"
image roommate angry_uniform = "images/Characters/[roommate] angry_uniform.png"
image roommate blushed_uniform = "images/Characters/[roommate] blushed_uniform.png"
image roommate confused_uniform = "images/Characters/[roommate] confused_uniform.png"
image roommate happy_uniform = "images/Characters/[roommate] happy_uniform.png"
image roommate neutral_uniform = "images/Characters/[roommate] neutral_uniform.png"
image roommate sad_uniform = "images/Characters/[roommate] sad_uniform.png"
image roommate shocked_uniform = "images/Characters/[roommate] shocked_uniform.png"
image roommate sleepy_uniform = "images/Characters/[roommate] sleepy_uniform.png"

image dormmate admiring_casual = "images/Characters/[dormmate] admiring_casual.png"
image dormmate angry_casual = "images/Characters/[dormmate] angry_casual.png"
image dormmate blushed_casual = "images/Characters/[dormmate] blushed_casual.png"
image dormmate confused_casual = "images/Characters/[dormmate] confused_casual.png"
image dormmate happy_casual = "images/Characters/[dormmate] happy_casual.png"
image dormmate neutral_casual = "images/Characters/[dormmate] neutral_casual.png"
image dormmate sad_casual = "images/Characters/[dormmate] sad_casual.png"
image dormmate shocked_casual = "images/Characters/[dormmate] shocked_casual.png"
image dormmate sleepy_casual = "images/Characters/[dormmate] sleepy_casual.png"
image dormmate admiring_uniform = "images/Characters/[dormmate] admiring_uniform.png"
image dormmate angry_uniform = "images/Characters/[dormmate] angry_uniform.png"
image dormmate blushed_uniform = "images/Characters/[dormmate] blushed_uniform.png"
image dormmate confused_uniform = "images/Characters/[dormmate] confused_uniform.png"
image dormmate happy_uniform = "images/Characters/[dormmate] happy_uniform.png"
image dormmate neutral_uniform = "images/Characters/[dormmate] neutral_uniform.png"
image dormmate sad_uniform = "images/Characters/[dormmate] sad_uniform.png"
image dormmate shocked_uniform = "images/Characters/[dormmate] shocked_uniform.png"
image dormmate sleepy_uniform = "images/Characters/[dormmate] sleepy_uniform.png"

image crush awkward_casual = "images/Characters/[crush] awkward_casual.png"
image crush angry_casual = "images/Characters/[crush] angry_casual.png"
image crush confused_casual = "images/Characters/[crush] confused_casual.png"
image crush happy_casual = "images/Characters/[crush] happy_casual.png"
image crush neutral_casual = "images/Characters/[crush] neutral_casual.png"
image crush sad_casual = "images/Characters/[crush] sad_casual.png"
image crush shocked_casual = "images/Characters/[crush] shocked_casual.png"
image crush sleepy_casual = "images/Characters/[crush] sleepy_casual.png"
image crush awkward_uniform = "images/Characters/[crush] awkward_uniform.png"
image crush angry_uniform = "images/Characters/[crush] angry_uniform.png"
image crush confused_uniform = "images/Characters/[crush] confused_uniform.png"
image crush happy_uniform = "images/Characters/[crush] happy_uniform.png"
image crush neutral_uniform = "images/Characters/[crush] neutral_uniform.png"
image crush sad_uniform = "images/Characters/[crush] sad_uniform.png"
image crush shocked_uniform = "images/Characters/[crush] shocked_uniform.png"
image crush sleepy_uniform = "images/Characters/[crush] sleepy_uniform.png"
