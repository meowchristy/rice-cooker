#********CHARACTER DESCRIPTIONS********
char_desc = {"Aloy": "Formerly an outcast, now a hunter of unparalleled skill. Ready to do the right thing at any time.",
             "Wanderer": "A wayfaring figure whose identity is a mystery. He dresses like a mountain ascetic, but he certainly does not act the part."}

char_title = {"Collei": "Sprout of Rebirth", 
                   "Traveler": "Outlander"}

char_gender = {"Dehya": "Female", "Lisa": "Female", "Nahida": "Female", "Nilou": "Female", 
                    "Cyno": "Male", "Wanderer": "Male", 
                    "Traveler": "Chosen by Player"}

char_aff = {"Chongyun": "Tianheng Thaumaturges", 
            "Xinyan": "The Red Strings", 
            "Shenhe": "Cloud Retainer's Abode", 
            "Yanfei": "Yanfei Legal Consultancy"}

#********SKILLS********
ayato_skill_1 = "Kamisato Ayato shifts positions and enters the Takimeguri Kanka state. After this shift, he will leave a watery illusion at his original location. After it is formed, the watery illusion will explode if opponents are nearby or after its duration ends, dealing AoE Hydro DMG\n"
ayato_skill_2 = "Takimeguri Kanka\nIn this state, Kamisato Ayato uses his Shunsuiken to engage in blindingly fast attacks, causing DMG from his Normal Attacks to be converted into AoE Hydro DMG. This cannot be overridden. It also has the following properties:\nAfter a Shunsuiken attack hits an opponent, it will grant Ayato the Namisen effect, increasing the DMG dealt by Shunsuiken based on Ayato's current Max HP. The initial maximum number of Namisen stacks is 4, and 1 stack can be gained through Shunsuiken every 0.1s. This effect will be dispelled when Takimeguri Kanka ends.\nKamisato Ayato's resistance to interruption is increased.\nUnable to use Charged or Plunging Attacks.\nTakimeguri Kanka will be cleared when Ayato leaves the field. Using Kamisato Art: Kyouka again while in the Takimeguri Kanka state will reset and replace the pre-existing state."

dehya_skill_1 = "This art of Dehya's own invention changes its method of use depending on the combat situation.\n"
dehya_skill_2 = "Indomitable Flame\nThis skill will be unleashed should there be no Fiery Sanctum field created by Dehya herself present at the time.\nDeals AoE Pyro DMG, and creates a field known as Fiery Sanctum.\n"
dehya_skill_3 = "Ranging Flame\nThis skill will be unleashed should a Fiery Sanctum field created by Dehya herself already exist.\nDehya will perform a leaping attack, dealing AoE Pyro DMG before recreating a Fiery Sanctum field at her new position.\nA Fiery Sanctum field created this way will inherit the remaining duration of the previous field.\nRanging Flame can be used only once throughout a single Fiery Sanctum field's duration.\n"
dehya_skill_4 = "Fiery Sanctum\nWhen an opponent within a Fiery Sanctum field takes DMG, the field will unleash a coordinated attack, dealing AoE Pyro DMG to them based on Dehya's ATK and Max HP. This effect can be triggered once every 2.5s.\nActive characters within this field have their resistance to interruption increased, and when such characters take DMG, a portion of that damage will be mitigated and flow into Redmane's Blood. Dehya will then take this DMG over 10s. When the mitigated DMG stored by Redmane's Blood reaches or goes over a certain percentage of Dehya's Max HP, she will stop mitigating DMG in this way.\nOnly 1 Fiery Sanctum created by Dehya herself can exist at the same time."
dehya_burst_1 = "Unleashing her burning anger and casting her inconvenient blade aside, Dehya enters the Blazing Lioness state and increases her resistance to interruption.\nIn this state, Dehya will automatically and continuously unleash the Flame-Mane's Fists, dealing Pyro DMG based on her ATK and Max HP, and when its duration ends, she will unleash an Incineration Drive, dealing AoE Pyro DMG based on her ATK and Max HP.\n"
dehya_burst_2 = "If a Fiery Sanctum field created by Dehya's own Elemental Skill 'Molten Inferno' exists when this ability is unleashed, Dehya will retrieve it, and then create another field once Blazing Lioness's duration expires. This field will take on the retrieved field's duration at the moment of its retrieval.\nIn this state, Dehya will be unable to cast her Elemental Skill, or perform Normal, Charged, and Plunging Attacks. 'Normal Attack: Sandstorm Assault' and Elemental Skill 'Molten Inferno' will be replaced by 'Roaring Barrage.'\nRoaring Barrage\nUnleashing Roaring Barrage within 0.4s after each Flame-Mane's Fist strike will increase the speed at which the next Flame-Mane's Fist strike will be triggered."

freminet_skill_1 = "Does an upward thrust that will deal Cryo DMG and cause Freminet to enter Pers Timer for 10s.\nWhile Pers Timer is active, his Elemental Skill will turn into Shattering Pressure.\n"
freminet_skill_2 = "Shattering Pressure\nExecutes different sorts of attacks based on the Pressure level of Pers Timer, and then cancels Pers Timer.\nLevel 0: Unleashes a vertical cut that will deal Cryo DMG.\nLevels 1 to 3: Unleashes a vertical cut alongside Pers, dealing Cryo DMG and Physical DMG. DMG dealt scales based on Pressure level.\nLevel 4: Borrows the power of a fully-pressurized Pers to deal Physical DMG. Meanwhile, Normal Attack: Flowing Eddies will be replaced by Shattering Pressure.\nPers Timer\nWhen Freminet uses Normal Attacks, he will also unleash waves of frost that deal Cryo DMG and increase Pers' Pressure level.\nThe accompanying Cryo DMG dealt this way is considered Elemental Skill DMG.\n"
freminet_skill_3 = "Arkhe: Pneuma\nAt certain intervals, after using the upward thrust, a Spiritbreath Thorn in the form of another upward thrust will be created, dealing Pneuma-aligned Cryo DMG.\nTo immobilize one's opponent without taking their life can also be considered something of a \"survival\" strategy that one may choose.\n\"Pers... I leave the rest to you.\""

kirara_skill_1 = "Press\nLeaps into the air with all the agility of a cat passing through the bushes, and thwacks her foes with a flying kick that deals AoE Dendro DMG while creating a Shield of Safe Transport. This will also briefly apply Dendro to Kirara. The shield will absorb Dendro DMG with 250% effectiveness. The shield's DMG absorption will be based on Kirara's Max HP and will not exceed a certain percentage of that Max HP. The remaining DMG absorption on a Shield of Safe Transport will stack on a new one when it is created, and its duration will reset.\n"
kirara_skill_2 = "Hold\nOut of her desire to \"deliver within half a day,\" Kirara deploys a Shield of Safe Transport identical to the one that can be created by pressing the skill. She will also curl up into a special express delivery box, entering the Urgent Neko Parcel state in order to move and fight more swiftly.\n"
kirara_skill_3 = "Urgent Neko Parcel\nDeals Dendro DMG to opponents she crashes into. This effect can be triggered once on each opponent every 0.5s.\nWhen in this state, Kirara's movement speed, climbing speed, and jumping power are all increased, and her Stamina Consumption from climbing is increased.\nWhen the duration ends or the skill is used again, a Flipclaw Strike more powerful than the attack in the Press Mode will be unleashed, dealing AoE Dendro DMG.\nThe Urgent Neko Parcel state lasts a maximum of 10s. When the state ends, the skill will enter CD. The longer Kirara spends in this state, the longer the CD will be.\nSprinting or actively canceling climbing will end this state early.\n\"So you wanna know the secret to speedy deliveries? Well, it's all in the legs!\""

kuki_3rd_passive = "Gains 25% more rewards when dispatched on an Inazuma Expedition for 20 hours."

layla_skill_1 = "Puts forth a shield known as the Curtain of Slumber, dealing AoE Cryo DMG.\nThe Curtain of Slumber's DMG Absorption is based on Layla's Max HP and absorbs Cryo DMG with 250% effectiveness. When the shield is deployed, Layla will have Cryo applied to her briefly.\n"
layla_skill_2 = "Night Stars and Shooting Stars\nWhile the Curtain of Slumber is active, it will create 1 Night Star that will be attached to it every 1.5s. When a character protected by this shield uses an Elemental Skill, 2 Night Stars will be created. Night Stars can be created once every 0.3s in this way. A maximum of 4 Night Stars can be accumulated at any one time.\nOnce the Curtain of Slumber has accumulated 4 Night Stars and there are opponents nearby, these Night Stars will transform into homing Shooting Stars that will be fired off in sequence, dealing Cryo DMG to any opponents hit.\nIf the Curtain of Slumber's duration ends or it is destroyed, the Night Stars will disappear. If they are already being fired off as Shooting Stars, these Shooting Stars will last until this wave of shots ends.\nNew Night Stars cannot be created until the previous wave of Shooting Stars has been fired completely."

lynette_skill_1 = "Flicks her mantle and executes an Enigma Thrust, dealing Anemo DMG.\nWhen the Enigma Thrust hits an opponent, it will restore Lynette's HP based on her Max HP, and in the 4s afterward, she will lose a certain amount of HP per second.\nBased on whether you press or hold this ability, she will use Enigma Thrust differently.\n"
lynette_skill_2 = "Press\nShe swiftly uses an Enigma Thrust.\n"
lynette_skill_3 = "Hold\nLynette will enter a high-speed Pilfering Shadow state and apply Shadowsign to a nearby opponent.\nWhen this high-speed state ends, Lynette will unleash her Enigma Thrust. If there is an opponent with Shadowsign applied to them nearby, Lynette will approach them in a flash before using Enigma Thrust.\nA maximum of 1 opponent can have Shadowsign at any one time. When this opponent gets too far from Lynette, the Shadowsign will be canceled.\n"
lynette_skill_4 = "Arkhe: Ousia\nAt specific intervals, Lynette will unleash a Surging Blade when she uses Enigma Thrust, dealing Ousia-aligned Anemo DMG.\n\"Now then, turn your eyes to the stage and continue to enjoy the performance. When I next appear, I'll be where you least expect.\""

lyney_atk_1 = "Normal Attack\nPerforms up to 4 consecutive shots with a bow.\nPlunging Attack\nFires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact.\nCharged Attack\nPerforms a more precise Aimed Shot with increased DMG.\nWhile aiming, flames will run across the arrowhead before being fired. Different effects will occur based on the time spent charging.\nCharge Level 1: Fires off a Pyro-infused arrow, dealing Pyro DMG.\nCharge Level 2: Fires off a Prop Arrow that deals Pyro DMG, and upon hit, it will summon a Grin-Malkin Hat.\nWhen firing the Prop Arrow, and when Lyney has more than 60% HP, he will consume a portion of his HP to obtain 1 Prop Surplus stack. Max 5 stacks. The effect will be removed after the character spends 30s out of combat.\nThe lowest Lyney can drop to through this method is 60% of his Max HP.\n"
lyney_atk_2 = "Grin-Malkin Hat\nCan taunt nearby opponents and attract their attacks. Each opponent can only be taunted by the Hat once every 5s.\nThe Hat will inherit a percentage of Lyney's Max HP.\nIf destroyed, or if its duration expires, it will fire off a Pyrotechnic Strike at 1 nearby opponent, dealing Pyro DMG.\n1 Hat can exist at any given time.\n"
lyney_atk_3 = "Arkhe: Pneuma\nAt certain intervals, the Prop Arrow will cause a Spiritbreath Thorn to descend upon its hit location, dealing Pneuma-aligned Pyro DMG."

nahida_skill_1 = "Sends forth karmic bonds of wood and tree from her side, dealing AoE Dendro DMG and marking up to 8 opponents hit with the Seed of Skandha. When held, this skill will trigger differently.\n"
nahida_skill_2 = "Hold\nEnters Aiming Mode, which will allow you to select a limited number of opponents within a limited area. During this time, Nahida's resistance to interruption will be increased.\nWhen released, this skill deals Dendro DMG to these opponents and marks them with the Seed of Skandha.\nAiming Mode will last up to 5s and can select a maximum of 8 opponents.\nSeed of Skandha\n"
nahida_skill_3 = "Opponents who have been marked by the Seed of Skandha will be linked to one another up till a certain distance.\nAfter you trigger Elemental Reactions on opponents who are affected by the Seeds of Skandha or when they take DMG from Dendro Cores (including Burgeon and Hyperbloom DMG), Nahida will unleash Tri-Karma Purification on the opponents and all connected opponents, dealing Dendro DMG based on her ATK and Elemental Mastery.You can trigger at most 1 Tri-Karma Purification within a short period of time."

nilou_skill_1 = "Nilou will enter the Pirouette state, dealing Hydro DMG to nearby opponents based on her Max HP.\nWhile she is in the Pirouette state, Nilou's Normal Attacks and Elemental Attacks will cause her to enter the Sword Dance and Whirling Steps stances respectively, causing DMG she deals to be converted to Hydro DMG that cannot be overridden and that is considered Elemental Skill DMG.\n"
nilou_skill_2 = "In these stances, Nilou's third dance step will end Pirouette, and has the following effects:\nSword Dance: unleashes a Luminous Illusion that deals Hydro DMG to opponents it touches and grants Nilou the Lunar Prayer effect. This effect converts Nilou's Normal Attacks into Sword Dance techniques, and her final hit will unleash a Luminous Illusion.\nWhirling Steps: Nilou unleashes a Whirling Water Wheel that deals AoE Hydro DMG and creates a Tranquility Aura that follows your active character around and applies Wet to opponents within its AoE.\nNilou is unable to perform Charged Attacks when under the effect of Pirouette or Lunar Prayer. These effects will be removed once she leaves the field."

raiden_burst_1 = "Gathering truths unnumbered and wishes uncounted, the Raiden Shogun unleashes the Musou no Hitotachi and deals AoE Electro DMG, using Musou Isshin in combat for a certain duration afterward. The DMG dealt by Musou no Hitotachi and Musou Isshin's attacks will be increased based on the number of Chakra Desiderata's Resolve stacks consumed when this skill is used.\n"
raiden_burst_2 = "Musou Isshin\nWhile in this state, the Raiden Shogun will wield her tachi in battle, while her Normal, Charged, and Plunging Attacks will be infused with Electro DMG, which cannot be overridden. When such attacks hit opponents, she will regenerate Energy for all nearby party members. Energy can be restored this way once every 1s, and this effect can be triggered 5 times throughout this skill's duration.\nWhile in this state, the Raiden Shogun's resistance to interruption is increased, and she is immune to Electro-Charged reaction DMG.\nWhile Musou Isshin is active, the Raiden Shogun's Normal, Charged, and Plunging Attack DMG will be considered Elemental Burst DMG.\nThe effects of Musou Isshin will be cleared when the Raiden Shogun leaves the field.\n"
raiden_burst_3 = "Chakra Desiderata\nWhen nearby party members (excluding the Raiden Shogun herself) use their Elemental Bursts, the Raiden Shogun will build up Resolve stacks based on the Energy Cost of these Elemental Bursts.\nThe maximum number of Resolve stacks is 60. The Resolve gained by Chakra Desiderata will be cleared 300s after the Raiden Shogun leaves the field."

sayu_skill_1 = "The special technique of the Yoohoo Ninja Arts!\nSayu curls up into a rolling Fuufuu Windwheel and smashes into opponents at high speed, dealing Anemo DMG.\nWhen the duration ends, she unleashes a Fuufuu Whirlwind Kick, dealing AoE Anemo DMG.\n"
sayu_skill_2 = "Press: Enters the Fuufuu Windwheel state, rolling forward a short distance before using the Fuufuu Whirlwind Kick.\n"
sayu_skill_3 = "Hold: Rolls about continuously in the Fuufuu Windwheel state, increasing Sayu's resistance to interruption while within that state.\nDuring this time, Sayu can control the direction of her roll, and can use the skill again to end her Windwheel state early and unleash a stronger version of the Fuufuu Whirlwind Kick.\nThe Hold version of this skill can trigger Elemental Absorption.\nThis skill has a maximum duration of 10s and enters CD once its effects end. The longer Sayu remains in her Windwheel state, the longer the CD.\nElemental Absorption: If Sayu comes into contact with Hydro, Pyro, Cryo and Electro while in her Windwheel state, she will deal additional elemental DMG of that type.\nElemental Absorption may only occur once per use of this skill."

shenhe_skill = "The frosted dew, silvery and dense, shall exorcise all demons.\nGrants all nearby party members the Icy Quill effect and deals Cryo DMG in different ways based on whether it is tapped, pressed, or held.\nPress\nRushes forward together with a Talisman Spirit, dealing Cryo DMG to opponents along the path.\nHold\nCommands the Talisman Spirit to deal AoE Cryo DMG.\nIcy Quill\nWhen Normal, Charged, and Plunging Attacks, Elemental Skills, and Elemental Bursts deal Cryo DMG to opponents, the DMG dealt is increased based on Shenhe's current ATK.\nThe Icy Quill's effects will be cleared once its duration ends or after being triggered a certain number of times. When held rather than tapped or pressed, the Icy Quill's effect lasts longer and can be triggered more times.\nWhen one Cryo DMG instance strikes multiple opponents, the effect is triggered multiple times based on the number of opponents hit. The number of times the effect is triggered is calculated independently for each party member with the Icy Quill."

wanderer_skill_1 = "Concentrates the power of the winds to break free from the shackles of the earth, dealing AoE Anemo DMG before leaping into the air and entering the Windfavored state.\n"
wanderer_skill_2 = "Windfavored\nThe Wanderer cannot perform Plunging Attacks in this state. When he uses Normal and Charged Attacks, they will be converted into Kuugo: Fushoudan and Kuugo: Toufukai respectively; the DMG they deal and their AoE will be increased, and their DMG will be considered Normal and Charged Attack DMG respectively. Kuugo: Toufukai will not consume Stamina. The Wanderer will hover persistently during this time.\n"
wanderer_skill_3 = "Windfavored (II)\nWhile this state is active, the Wanderer's movements gain the following properties:\n- Persistently consumes Kuugoryoku Points to maintain this hovering state.\n- When sprinting, additional Kuugoryoku Points will be consumed for the Wanderer to accelerate mid-air. Holding sprint will cause persistent Kuugoryoku Point consumption to maintain speed. This effect will replace his default sprint.\n- Jumping expends extra Kuugoryoku Points to increase hovering height. Holding jump will cause persistent Kuugoryoku Point consumption to keep increasing hovering height.\nRunning out of Kuugoryoku Points will end the Windfavored state. A second cast during the duration of Windfavored will also end it."

yaoyao_skill_1 = "Calls upon “Yuegui: Throwing Mode,” a special device created by a certain adeptus to help Yaoyao solve her problems.\nThis skill will be used differently in Holding Mode.\n"
yaoyao_skill_2 = "Hold\nEnters Aiming Mode to adjust the throw direction.\n"
yaoyao_skill_3 = "Yuegui: Throwing Mode\nThrows out White Jade Radishes that will explode upon hitting characters or opponents, dealing Dendro DMG to opponents within a certain AoE, and healing characters within that same AoE based on Yaoyao’s Max HP. If a radish does not hit either an opponent or a character, the radish will remain where it is and explode on contact with a character or opponent, or will explode after its duration expires.\nYuegui: Throwing Mode will choose its radish-throw targets.\n·If all nearby characters have more than 70% HP remaining, then it will throw the radish at a nearby opponent.\n·If nearby characters have 70% or less HP remaining, it will throw a radish at the character with the lowest HP percentage remaining. If no opponents exist nearby, Yuegui will also throw White Jade Radishes at characters if they all have more than 70% HP and less than 100% HP remaining. Otherwise, it will throw radishes into the area at random.\nA maximum of 2 instances of Yuegui: Throwing Mode can exist at any one time."

zhongli_skill_1 = "Press\nCommands the omnipresent power of earth to solidify into a Stone Stele, dealing AoE Geo DMG.\nAdditionally, the Stone Stele will resonate with other Geo Constructs in the vicinity, dealing Geo DMG to surrounding enemies.\nThe Stone Stele is considered a Geo Construct, and can both be climbed and used to block attacks. Only one may exist at any one time.\n"
zhongli_skill_2 = "Hold\nCauses nearby Geo energy to explode, causing the following effects:\nCreates a shield of jade. The shield's DMG Absorption scales based on Zhongli's Max HP, and absorbs Geo DMG 250% more effectively.\nCauses AoE Geo DMG.\nIf there are nearby targets with the Geo element, it will drain a large amount of Geo element from a maximum of 2 such targets. This effect does not cause DMG.\n"
zhongli_skill_3 = "Stone Stele\nWhen created, deals AoE Geo DMG.\nAdditionally, it will intermittently resonate with other nearby Geo constructs, dealing Geo DMG to nearby opponents.\nThe Stone Stele is considered a Geo construct that can both be climbed and used to block attacks.\nOnly one Stele created by Zhongli himself may initially exist at any one time.\n"
zhongli_skill_4 = "Jade Shield\nPossesses 150% DMG Absorption against all Elemental and Physical DMG.\nCharacters protected by the Jade Shield will decrease the Elemental RES and Physical RES of opponents in a small AoE by 20%. This effect cannot be stacked."

#********NATIONS********
nations_dict = {"Mondstadt": "A city of freedom that lies in the northeast of Teyvat.\nFrom amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions — a gift from the Anemo God, Barbatos — across Cider Lake to Mondstadt, which sits on an island in the middle of the lake.", 
                "Liyue": "A bountiful harbor that lies in the east of Teyvat.\nMountains stand tall and proud alongside the stone forest, that, together with the open plains and lively rivers, make up Liyue's bountiful landscape, which shows its unique beauty through each of the four seasons. Just how many gifts from the Geo God lie in wait amongst the rocks of Liyue's mountains?", 
                "Inazuma": "An Isolated Archipelago Far East of Teyvat.\nOvercome endless thunderstorms and set foot on the islands of red maple and cherry blossoms. On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho.", 
                "Sumeru": "The city of scholars located in the west-central part of Teyvat.\nA fantastical nation of both lush rainforest and barren desert, where countless fruits of wisdom grow and are buried. Whether Travelers travel from afar through the forest to reach the academy city or delve deep into the desert to discover the historical ruins of the red desert, a wealth of valuable knowledge awaits them here."}



#********ELEMENTS********
elements_dict = {"Anemo": "The name Anemo comes from the prefix for words related to wind, \"anemo-,\" which derives from the Ancient Greek word for wind (Ancient Greek: ἄνεμος ánemos).\n\- Genshin Impact Wiki", 
                 "Cryo": "The name Cryo comes from the prefix for words related to freezing or ice, \"cryo-,\" which derives from the Ancient Greek word for icy cold, frost, chill (Ancient Greek: κρύος krúos).\n\- Genshin Impact Wiki", 
                 "Dendro": "The name Dendro comes from the prefix used in biology for scientific names related to trees or plants, \"dendro-,\" which derives from the Ancient Greek word for tree (Ancient Greek: δένδρον déndron).\n\- Genshin Impact Wiki", 
                 "Electro": "The name Electro comes from the prefix for words related to electricity, \"electro-,\" which derives from the Ancient Greek word for amber (Ancient Greek: ἤλεκτρον ḗlektron) (a natural resin, which — when rubbed — produces static electricity).\n\- Genshin Impact Wiki", 
                 "Geo": "The name Geo comes from the prefix for words related to the Earth, \"geo-,\" which derives from the Ancient Greek word for earth (Ancient Greek: γῆ gê).\n\- Genshin Impact Wiki", 
                 "Hydro": "The name Hydro comes from the prefix for words related to water, \"hydro-,\" which derives from the Ancient Greek prefix for words related to water (Ancient Greek: υδρο- ydro-) which in turn derives from the Ancient Greek word for water (Ancient Greek: ὕδωρ húdōr).\n\- Genshin Impact Wiki", 
                 "Pyro": "The name Pyro comes from the prefix for words related to fire, \"pyro-,\" which derives from the Ancient Greek word for fire (Ancient Greek: πῦρ pûr).\n\- Genshin Impact Wiki", 
                 "Bloom": "When creatures are affected by Hydro and Dendro, the Bloom reaction will be triggered, creating Dendro Cores. Only a certain number of Dendro Cores can exist at the same time. If new ones are created once this limit is reached, or if the duration of the existing Dendro Cores ends, the pre-existing Dendro Cores will burst, dealing AoE Dendro DMG...", 
                 "Burgeon": "When Dendro Cores come into contact with Pyro, they will trigger Burgeon, causing even greater AoE Dendro DMG.", 
                 "Hyperbloom": "When Dendro Cores come into contact with Electro, they will trigger Hyperbloom and transform into homing Sprawling Shots.", 
                 "Catalyze": "When creatures are affected by Electro and Dendro, Quicken will occur, which will render them Quickened. When Quickened creatures are affected by Electro or Dendro attacks, the Aggravate or Spread reactions will occur respectively, causing them to take additional DMG."}

#********ENEMIES********
enemy_dict = {"Abyss Heralds": "Abyss Heralds are an elite enemy group part of the Abyss Order and who are capable of manipulating intense abyssal energy. They are melee counterparts to Abyss Lectors, though they also have some ranged attacks at their disposal.\n\- Genshin impact Wiki", 
              "Cicin": "Cicins are Common Enemies found across Teyvat. They appear as small bat-like creatures.\n\- Genshin Impact Wiki", 
              "Consecrated Beast": "Consecrated Beasts are an elite enemy group. While the majority can be found in Sumeru, they can also be found in Inazuma and Fontaine.\n\nThey are wildlife that have grown larger and stronger as a result of mutations from eating greater lifeforms, such as gods and surviving the highly painful process. As a result of being unable to fully consume said lifeforms, they have grown bone-like features across their bodies.\n\- Genshin Impact Wiki", 
              "Defense Mechanism": "The Defense Mechanism is a Unique Enemy found in Dragonspine.\n\nIt resembles a spherical automaton with a petal-like head, and a tail on its back. It is similar to the sign on the door of a Domain. When inactive, they fold their petals and lie on the ground.\n\- Genshin Impact Wiki", 
              "Floating Fungus": "Floating Fungi are Common Enemies that are part of the Fungi enemy group and the Mystical Beasts family.\n\- Genshin Impact Wiki", 
              "Grounded Shroom": "Grounded Fungi are Common Enemies that are part of the Fungi enemy group and the Mystical Beasts family.\n\- Genshin Impact Wiki", 
              "Hilichurl Shooter": "Hilichurl Shooters are Common Enemies that are part of the Hilichurl Shooters enemy group and the Hilichurls family.\n\- Genshin Impact Wiki", 
              "Kairagi": "Kairagi (Japanese: 海かい乱ら鬼ぎ Kairagi), are a type of Nobushi.\n\- Genshin Impact Wiki", 
              "Primal Construct": "Primal Constructs are an elite enemy group. As leftover technology of King Deshret's civilization, they are primarily found across the Great Red Sand.\n\-Genshin Impact Wiki",
              "Ruin Drake": "Ruin Drakes are an enemy group found in Sumeru and Fontaine. As their name indicates, their appearance and abilities of these Ruin Machines are inspired by dragons and vishaps.\n\- Genshin Impact Wiki", 
              "Ruin Sentinel": "Ruin Sentinel is an enemy group of Automatons found in the regions of Inazuma, Enkanomiya, The Chasm: Underground Mines, and Sumeru and are usually found in groups. They are designed to mimic different organisms found in Teyvat.\n\- Genshin Impact Wiki", 
              "Winged Shroom": "Winged Cryoshrooms are Common Enemies that are part of the Fungi enemy group and the Mystical Beasts family.\n\- Genshin Impact Wiki", 
              "Samachurl": "Samachurls are shamans and spiritual leaders of Hilichurl tribes.\n\-Genshin Impact Wiki", 
              "Treasure Hoarder": "The Treasure Hoarders are a gang of bandits who search for treasures to obtain and are located all around Teyvat.\n\- Genshin Impact Wiki", 
              "The Great Snowboar King": "A special enemy and miniboss in Dragonspine, located to the East of Entombed City - Ancient Palace, south of the word 'Ancient' on the map, and is part of the 'Ah, Fresh Meat!' World Quest\n\- Genshin Impact Wiki", 
              "The Eremite": "A group of people who hail from Sumeru's desert region. Most of them are mercenaries by trade and conduct business across Teyvat.\n\- Genshin Impact Wiki", 
              "Whirling Fungus": "Whirling Fungi are Common Enemies that are part of the Fungi enemy group and the Mystical Beasts family.\n\- Genshin Impact Wiki", 
              "Stretchy Fungus": "Stretchy Geo Fungi are Common Enemies that are part of the Fungi enemy group and the Mystical Beasts family.\n\- Genshin Impact Wiki"}

#********RARITY********
rarity_dict = {5: "★★★★★", 4: "★★★★", 3: "★★★", 2: "★★", 1: "★"}

colors_dict = {5: 0xd49548, 4: 0x935c9d, 3: 0x5d839a, 2: 0x5d8771, 1: 0x7f7d81, 
               "Pyro": 0xea7838, "Cryo": 0xa4d6e3, "Electro": 0xb38dc1, "Geo": 0xf2b723, "Dendro": 0x9cc928, "Hydro": 0x5fc1f1, "Anemo": 0x71c2a7}

#********CONSUMABLES********
kitty_meal = "This main dish looks rather cute. The simple methodology used to make it has maximized flavor retention in its ingredients. Even cats who usually pay humdrum humanity little mind will surely come running over when they catch a whiff of this. Uh, wait a moment. Was this supposed to attract dogs, too?"

potion_desc = {"Flaming Essential Oil": "Grants greater affinity for Pyro, boosting Pyro DMG.\nIt is made of materials that gestate Pyro, which serves to draw in Pyro energy more effectively. It also makes the user more fired-up and passionate.", 
               "Streaming Essential Oil": "Grants greater affinity for Hydro, boosting Hydro DMG.\nIt's a slippery medicine for external use, able to better channel Hydro energy. It has a subtle fragrance.", 
               "Frosting Essential Oil": "Grants greater affinity for Cryo, boosting Cryo DMG.\nIt has a chilling sensation when applied, and helps one to better channel Cryo energy. It also helps to keep you cool-headed and calm.",
               "Gushing Essential Oil": "Grants greater affinity for Anemo, boosting Anemo DMG.\nIt has a fragrant smell. It is said that using it during your travels will make you walk as if you're riding on the wind.", 
               "Shocking Essential Oil": "Grants greater affinity for Electro, boosting Electro DMG.\nIt induces a tingling sensation on the skin and renders the user better able to better channel Electro energy — but comes with a risk of causing an electrical fire that would definitely ruin your perfect hair.", 
               "Unmoving Essential Oil": "Grants greater affinity for Geo, boosting Geo DMG.\nYou can feel the fine Geo pellets within when applied. It's said to help with physical injuries.", 
               "Forest Essential Oil": "Grants greater affinity for Dendro, boosting Dendro DMG.\nIt's a nourishing external medicine that promotes growth of plants, able to better channel Dendro energy.", 
               "Heatshield Potion": "A miraculous potion that boosts Pyro RES and makes one able to withstand high heat. \nIt works not by cooling the body, but by helping the body acclimate to high temperatures.",
               "Desiccant Potion": "A kind of potion that boosts Hydro RES and makes one able to withstand highly humid environments. \nIt is said to act like a desiccant and be highly effective at keeping items dry. It can also be ingested for the same effect.",
               "Frostshield Potion": "A miraculous potion that boosts Cryo RES and makes one able to withstand extreme cold. \nInduces a chilling sensation when drank, but once this sensation spreads throughout the body, the feeling of being cold disappears.",
               "Windbarrier Potion": "A mysterious potion that boosts Anemo RES and makes one able to withstand strong winds. \nIt works wonders for adventurers out in the world and is even said to keep the cold away.",
               "Insulation Potion": "A potion that boosts Electro RES and keeps one from getting electro-shocked. Induces a tingling sensation when drank. \nIt is said to work by filling the body with inversely charged electrical energy, which counteracts the effect of Electro damage.",
               "Dustproof Potion": "A potion that boosts Geo RES and keeps one from getting bothered by sand and dust. It has a strange taste not unlike that of magnets. \nIt keeps a traveler clean from all the sand and dust out there.",
               "Dendrocide Potion": "A potion that boosts Dendro RES and suppresses the growth of plants. Rather than killing the plants, it puts them in deep hibernation. \nIt's also said to be good for the body if ingested.", 
}

bm = {"Hurricane Seed": "The imploded form of an Anemo Hypostasis upon its defeat. It contains the essence of Anemo energy.\nIt is said that the power to create hurricanes resides within its seemingly fragile body. This butterfly of pure Anemo energy must be waiting for the day to conjure up storms once again.",
     "Lightning Prism": "An Electro Hypostasis channels nearby elemental energy to repair damaged elemental entities. Contains the essence of Electro energy.\nA common prism separates white light into component colors; a Lightning Prism, however, channels flowing energy and weaves them into lightning. It will continue to do so even after the Electro Hypostasis has been defeated.",
     "Basalt Pillar": "A pillar formed by the shell of a Geo Hypostasis, composed of high-density Geo energy. It is a testament to Geo's status as the heaviest of the elements. Maybe the reason a Geo Hypostasis creates this pillar out of its shell and raises itself is just to get closer to the sky, not to combat enemies.",
     "Hoarfrost Core": "The exposed core of a defeated Cryo Regisvine. Pure Cryo elements are contained within it. Energy and thoughts that swell deep within the earth will eventually erupt on the surface. Even the deathly silent frost will attach to living things on the ground, turning even ordinary vegetation like vines into huge, vicious predators.",
     "Everflame Seed": "A seed that fuels the unending flames of the Pyro Regisvine. It emits Pyro energy as if it will burn all that has ever sprouted from the ground.\nEndless desires flow among turbulent energy deep within the earth. What desire could steadily hold such fire to the plants and long so eagerly to bathe everything in unquenchable flames?",
     "Cleansing Heart": "A palmful of eternal water left by an oceanid.\nThough it has already diffused among the depths of the lake, its purity remains all the same. But why would a creature so pure and clean as an oceanid covet the appearance of a being that roams the land, and assume such a form with pure water? They need not breathe nor do they require sustenance...",
     "Juvenile Jade": "A crystalline substance taken from a Primo Geovishap. Within it is contained the potential to become a dragon.\nThese dull crystals are precipitated within the bodies of vishaps sleeping in the mountains. Liyue folklore holds that they will gather power over many years, after which this crystal will, at last, replace their original heart, and the vishap will become a true dragon — one that can shake the mountains and split the earth.",
     "Crystalline Bloom": "An ice crystal of exceeding purity that is created in the frigid blooming of a Cryo Hypostasis.\nThese frosty crystals will continue to grow according to their own cold, rigid laws, till one day a flower of winter shall bloom and freeze everything. Perhaps it is stagnant time, that never-thawing bosom, that is the essence of this undying flower.",
     "Marionette Core": "This core can power the inorganic Maguu Kenki and cause it to wield a blade like a living being.\nFlesh decays, and with it decay all martial arts mastery and all poignant memories.\nPerhaps only by converting one's four limbs and body into sturdy mechanical parts, and by at last sacrificing one's very own heart for a sophisticated mechanical one, can one transcend the impermanence of the fleshly form...",
     "Perpetual Heart": "The core that powers the autonomous movements of the Perpetual Mechanical Array.\nSome theorize that the symbols on these cores have knowledge and logic inscribed upon them in a language that eyes cannot perceive. Some go a step further and believe that these unique Ruin machines autonomously decided to forsake a biomimetic form to pursue strength of function on account of their especially large cores and complex inscriptions.",
     "Smoldering Pearl": "A crystallization of a Pyro Hypostasis that constantly emits heat.\nEven the burning flames shall one day grow cold, and even the ashen firewood can will itself back into a raging blaze. It must then be the will of the world that Pyro Hypostases should constantly cool down and heat up, much like the universe teems with endless life... until the fated darkness shall one day descend and bring it all to naught.",
     "Dew of Repudiation": "A strange water droplet left behind by the collapse of the Hydro Hypostasis.\nIt has strong rejection properties, and this forms the basis of one of the Hydro Hypostasis' attack patterns as well. They say that water contains memories and willpower, and that these things can grow when bodies of water meld together. However, the waves conjured by the Hydro Hypostasis are incompatible with the currents that flow above and below ground. Even if it were to flow into the surpassingly pure waters of Petrichor, this drop of water will likely resist assimilation as strongly as mercury.",
     "Storm Beads": "Crackling Electro pearls left behind by the Thunder Manifestation.\nIt is said that Thunder Manifestations will only descend upon lands where powerful hatred dwells. The singers say that it is the unbearable disappointments and sufferings of life that drive them to forever wander the broken earth, unleashing sky-searing lightning as they go.",
     "Riftborn Regalia": "A broken horn that you obtained from defeating the Wolflord. That said, it should not have left anything behind after your hunt.\nEven a lord among the Riftwolves is nothing before monsters of a higher pedigree.\n\"Gold\" mass-produced these malformed wolf packs almost as if by accident, like shrunken drawings on discarded sheets of paper, and the horns on this one represent its authority to command its dark brood to dissolve space itself.",
     "Dragonheir's False Fin": "A piece of biological tissue that you found after defeating the Bathysmal Vishaps.\nAlthough it looks like a fin of some kind, it does not actually have any function at all\nThe people of Byakuyakoku once investigated the Bathysmal Vishaps quite deeply. Their most distinctive feature was the ability to choose what traits it wished to pass on to its offspring. Because of their great hatred for humanity, these vishaps will lose any visual acuity by the time they reach maturity. At the same time, they have evolved a certain degree of elemental polymorphism for combat purposes.",
     "Runic Fang": "A \"fang\" with which the mysterious, snakelike machine of old dug into mountains' depths. There are many ominous runes carved on it.\nIt is said that giant serpents lurk in the dark fissures deep beneath the ground. Burning with eternal resentment and malice toward the world above, they throw themselves into digging great tunnels, yet none know what their malicious purposes are…",
     "Majestic Hooked Beak": "An elongated bill that you found after defeating the Jadeplume Terrorshroom.\nResearchers still consider it a miracle even now that some soft Fungi have evolved these rock-hard hooked beaks. This magnificent king amongst Fungi has been leisurely pacing on the finish line of evolution. Now and then, it emits a long call to all the living beings in the rainforest: Even the most helpless and timid creature may one day become the monarch of the woods.",
     "Thunderclap Fruitcore": "The core of an Electro Regisvine, wrapped in razor-sharp leaves, wantonly emits Electro energy.\nThe roaring energy rampaging deep within the earth is eager to pour out its rage, thus even tainting these unfortunate vines with its mania, causing them to wail and flail their branches frantically. One can hardly tell whether it longs for others to taste the pain of being continuosly electrocuted and charred or if it is struggling, looking forward to its inevitable doom.",
     "Perpetual Caliber": "A motive device obtained from a mysterious ruin machine.\nThe machine it once powered may have been destroyed, but it continues to rotate all the same.\nThere should be no such thing as an energy source that can sustain itself forever in this world, and most research results obtained in the field of \"perpetual motion\" have been eventually proved false. Yet, this device is proof that a now-destroyed civilization once reached heights that present-day nations could not hope to match...",
     "Light Guiding Tetrahedron": "A core component obtained via defeating a mysterious ruin machine.\nTo this day, these ancient devices have not forgotten the dreams of their masters or their own duties: to build a thousand palaces, to administrate three thousand machines, to sow ten thousand flowers that shall never bloom again, and to recreate a paradise now buried beneath the desert sands for the sake of all who live in this world.\nThough the lord of the desert no longer lives, and those dreams have long been corrupted by sinful whispers, and though all the magical pillars have been broken and have collapsed, the great beast once favored by the king hides still within the great searing storm.",
     "Quelled Creeper": "The final coalesced form of the Dendro Hypostasis. The tough vines protect a pure cubic elemental crystal.\nDendro defies any common logic yet exists in perfect harmony with life. Elemental Hypostases, on the contrary, are most distant in appearance to all living beings. The combination of these two should probably never have appeared in this world. It is said that such elemental hypostases have the intelligence to \"learn\" and have thus understood the colors and dreams of the forest, a process that has transformed them into this shape over thousands of years.",
     "Psuedo-Stamens": "The pale wing-sheathes hiding in a Wenut's tail are as thin as the blooming stamens of a flower.\nIt is said that in the past, even before the beginning of time, they used to travel through the moist land under meadows and forests, similar to birds flying across the sky and fish swimming in the water. It is generally believed that their mimicry of flowers is to lure lost prey caught by sandstorms. There is also a theory, however, that their imitation of a blooming flower was inspired by the splendid blossoms countless epochs ago, which have long gone the way of the desert winds.",
     "Evergloom Ring": "A mystical weapon obtained after defeating the Four-Armed Envoy of dark tidings.\nRings are shaped like passageways, which is why arcane formations that are meant to produce some mystical effect are often ring-shaped. Such rings are perhaps gateways intended to guide the universe itself.",
     "Artificed Spare Clockwork Component — Coppelia": "An artificed spare clockwork component belonging to Coppelia. It powers this artificed dancer.\nAccording to its creator's design, the story of the artificed dancer with delicate joints ends at a merry moment. Coppelia will send whoever attempts to disturb that moment to a chapter of misfortune with her superb combat skills.",
     "Artificed Spare Clockwork Component — Coppelius": "An artificed spare clockwork component belonging to Coppelius. It powers this artificed dancer.\nThe artificed dancer whirls to a platinum tune, performing an unending waltz of icewind. Coppelius's dance will not stop. He will continue whirling till the bell tolls.",
     "Emperor's Resolution": "The war hammer of the Emperor of Fire and Iron. The mighty crab has crushed countless foes with this giant claw. Be it clockwork meka, other Fontemer Aberrants, or hunters with ill-placed curiosity — all have yielded under its power.\nFontemer Aberrants are different from human beings in that the concepts of aristocracy or inheritance are entirely foreign to them. None of them are born superior. One that survives deadly predators and adversities is able to accumulate infinite power as it keeps hunting and feeding over centuries. Such a creature is often referred to as an overlord for the fear it inspires."}

ca = {"Vayuda Turquoise Sliver": "Character Ascension Material.", 
     "Vayuda Turquoise Fragment": "Character Ascension material.\n\"Still, the winds change direction.\"", 
     "Vayuda Turquoise Chunk": "Character Ascension material.\n\"Still, the winds change direction.\nSomeday, they will blow towards a brighter future...\"", 
     "Vayuda Turquoise Gemstone": "Character Ascension material.\n\"Still, the winds change direction.\n\"Someday, they will blow towards a brighter future...\n\"Take my blessings and live leisurely from this day onward.\"", 
     "Shivada Jade Sliver": "Character Ascension Material.", 
     "Shivada Jade Fragment": "Character Ascension material.\n\"Sorry...\"", 
     "Shivada Jade Chunk": "Character Ascension material.\n\"Sorry...\"\n\"...to also have you shoulder the grievances of the world.\"", 
     "Shivada Jade Gemstone": "Character Ascension material.\n\"Sorry... to also have you shoulder the grievances of the world.\n\"Since you could endure my bitter cold, you must have the desire to burn?\n\"Then, burn away the old world for me.\"", 
     "Vajrada Amethyst Sliver": "Character Ascension material.", 
     "Vajrada Amethyst Fragment": "Character Ascension material. \n\"This body is the noblest and most eminent of all in this world.\"", 
     "Vajrada Amethyst Chunk": "Character Ascension material. \n\"This body is the noblest and most eminent of all in this world. It should hold absolute control over this world.\"", 
     "Vajrada Amethyst Gemstone": "Character Ascension material. \n\"This body is the noblest and most eminent of all in this world.\" \n\"It should hold absolute control over this world.\" \n\"It once promised its people a dream: the never-changing 'eternity.\"",
     "Nagadus Emerald Sliver": "Character Ascension material.", 
     "Nagadus Emerald Fragment": "Character Ascension material. \n\"I had a very, very long dream...\"", 
     "Nagadus Emerald Chunk": "Character Ascension material. \n\"I had a very, very long dream...\"\n\"In it, people were holding hands, dancing in a circle, be they sages or fools, dancers or warriors, puppets or statues of gods...\"", 
     "Nagadus Emerald Gemstone": "Character Ascension material. \n\"I had a very, very long dream...\"\n\"In it, people were holding hands, dancing in a circle, be they sages or fools, dancers or warriors, puppets or statues of gods...\"\n\"That dancing circle embodied everything about the universe. Life has always been the end, while it is wisdom that shall be the means.\"",
     "Prithiva Topaz Sliver": "Character Ascension Material.", 
     "Prithiva Topaz Fragment": "Character Ascension material. \n\"The currencies that flow through this land are my flesh and blood.\"",
     "Prithiva Topaz Chunk": "Character Ascension material.\n\"The currencies that flow through this land are my flesh and blood. \nFor thus did I become the guarantor of the people's hard work, wisdom, and future.\"",
     "Prithiva Topaz Gemstone": "Character Ascension material. \n\"The currencies that flow through this land are my flesh and blood. \nFor thus did I become the guarantor of the people's hard work, wisdom, and future. \nThis is the trust I have placed in them. Betray it, and you taint my blood.\"",
     "Varunada Lazurite Sliver": "Character Ascension Material.",
     "Varunada Lazurite Fragment": "Character Ascension material.\n\"My ideals have no stains.\"",
     "Varunada Lazurite Chunk": "Character Ascension material.\n\"My ideals have no stains. \nI must correct you. People here bear no sins in the ey,es of the gods...\"",
     "Varunada Lazurite Gemstone": "Character Ascension material.\n\"My ideals have no stains. \nI must correct you. People here bear no sins in the eyes of the gods... Only laws and the Tribunal can judge someone. \nThey can judge even me. So praise my magnificence and purity.\"",
     "Agnidus Agate Sliver": "Character Ascension Material.",
     "Agnidus Agate Gemstone": "Character Ascension material.\n\"A pilgrimage for a wish; a battle to earn a name...\nBurnt to cinders for a dream.\nIf the intention yet remains, achieved ▉▉'s truth he has.\"",
     "Agnidus Agate Fragment": "Character Ascension material. \n\"A pilgrimage for a wish; a battle to earn a name...\"",
     "Agnidus Agate Chunk": "Character Ascension material. \n\"A pilgrimage for a wish; a battle to earn a name...\nBurnt to cinders for a dream.\"",
     "Brilliant Diamond Sliver": "Character Ascension material. \n\"Welcome to this world.\"",
     "Brilliant Diamond Fragment": "Character Ascension material.\n\"Welcome to this world.\"",
     "Brilliant Diamond Chunk": "Character Ascension material.\n\"Welcome to this world.\"",
     "Brilliant Diamond Gemstone": "Character Ascension material.\n\"Welcome to this world.\"",
}
     
ce = {"Wanderer's Advice": "Character EXP material. Gives 1000 EXP.\nThese experiences are still beneficial even if one does not live in Teyvat.",
      "Adventurer's Experience": "Character EXP material. Gives 5000 EXP.\nThese experiences are very beneficial for journeys into the unknown.",
      "Hero's Wit": "Character EXP material. Gives 20000 EXP.\nThese experiences are extremely precious for a pilgrim traveling through Teyvat in order to be closer to Celestia.",
}

ls = {"calla-lily": 0,
      "cecilia": 1,
      "dandelion-seed": 2,
      "philanemo-mushroom": 3,
      "small-lamp-grass": 4,
      "valberry": 5,
      "windwheel-aster": 6,
      "wolfhook": 7,
      "cor-lapis": 0,
      "glaze-lily": 1,
      "jueyun-chili": 2,
      "noctilucous-jade": 3,
      "qingxin": 4,
      "silk-flower": 5,
      "starconch": 6,
      "violetgrass": 7,
      "amakumo-fruit": 0,
      "crystal-marrow": 1,
      "dendrobium": 2,
      "fluorescent-fungus": 3,
      "naku-weed": 4,
      "onikabuto": 5,
      "sakura-bloom": 6,
      "sango-pearl": 7,
      "sea-ganoderma": 8,
      "henna-berry": 0,
      "kalpalata-lotus": 1,
      "mourning-flower": 2,
      "nilotpala-lotus": 3,
      "padisarah": 4,
      "rukkhashava-mushrooms": 5,
      "sand-grease-pupa": 6,
      "scarab": 7,
      "trishiraite": 8,
      "beryl-conch": 0,
      "lumidouce-bell": 1,
      "rainbow-rose": 2,
      "romaritime-flower": 3}

ls_desc = {"Calla Lily": "A flower that grows near water sources. When cooked, the petals have a chunky texture, yet are sweet and a little bitter.",
      "Cecilia": "A beautiful flower with a name that suits its appearance. It only grows where harsh winds blow, and is just as intangible as the true heart of an unbound soul.",
      "Dandelion Seed": "A tiny seed that rides on the wind. Even without its feathered wings, it still holds the hope from afar within.",
      "Philanemo Mushroom": "A fungus that grows in the warm caress of the wind. It is as everlasting as the wind, nourishing life.",
      "Small Lamp Grass": "A wild grass that emits light at night. Used in cooking to enhance other flavors.",
      "Valberry": "A plump and translucent berry that has a fragrant smell and a sweet, refreshing taste. In the past, the storm watchers' only solace was the sweetness of this fruit and hope for the city's peace.",
      "Windwheel Aster": "A plant that adores the wind. To the proud children of the wind, or the citizens of Mondstadt, the Windwheel Asters are \"the visible winds.\"",
      "Wolfhook": "A berry with thorns that often gets attached to a wolf's pelt. When you look at it, you can almost hear the echoing cries of the wolves in the woods.",
      "Cor Lapis": "A precious crystal of condensed pure Geo element that usually grows along with other minerals. It's also commonly called \"Cor Petrae.\"",
      "Glaze Lily": "An extremely ancient flower that was said to be commonly seen in Liyue. It transforms the memories of the land into its fragrance during florescence.",
      "Jueyun Chili": "A spicy plant native to Liyue. Merely smelling it makes one hot and thirsty.",
      "Noctilucous Jade": "A rare mineral that glimmers in the dark. It's said to be a mutated gemstone condensed from the flourishing elements of the world.",
      "Qingxin": "A translucent white flower that only grows on the highest stone peaks. It eschews the warmth and moisture of the plains to gaze out afar from the solitary mountaintops.",
      "Silk Flower": "A crimson flower that blooms like the rainbow clouds in Liyue. It can be made into silky-smooth fabric.",
      "Starconch": "Empty seashells brought ashore by the tides. Hold it close to your ear, and hear the longing calls of the sea.",
      "Violetgrass": "A small flower with strong vitality. It is said that its downward-blooming flower keeps its fragrance from dissipating.",
      "Amakumo Fruit": "The fruit of the Amakumo Grass, which grows on Seirai Island. You can hear it crackling with a tiny current if you hold it up to your ear.",
      "Crystal Marrow": "A crystal that contains a sliver of Tatarigami power. Adding this material during smelting will greatly increase the strength and toughness of metals.",
      "Dendrobium": "A vibrant plant that has also been named the \"lycoris\" by the poets. It was once thought extinct in the Inazuman archipelago, only to re-emerge now upon the battlefields. It is said that it blooms most enchantingly where much blood was spilled.",
      "Fluorescent Fungus": "A mushroom that glows like a night-light. Some curious power lies hidden within it.",
      "Naku Weed": "Even on windless days, this plant will tremble lightly amid the cries of thunder. The parts of it that resemble petals are in fact extensions of the leaves meant to protect the fragile flower.",
      "Onikabuto": "A strange beetle that inhabits areas rich with Electro energy. Its docile and sedentary temperament could not be more different from the fierce, demonic visage displayed on its armored shell.",
      "Sakura Bloom": "Blossoms from the Sacred Sakura at the Grand Narukami Shrine, filled with a fondness for Inazuma.",
      "Sango Pearl": "A precious pearl that grows in the coral of Watatsumi. Gives off a cool sheen like that of the moonlight.",
      "Sea Ganoderma": "A plant species that only grows in certain regions and islands of the ocean. Though it looks like a fungus of some sort, it actually comes from a substance secreted by certain soft-bodied organisms.",
      "Henna Berry": "A fruit that grows even in the most hostile of desert environments. Its vibrant crimson fruits are made even more lovely against a backdrop of yellow sand.",
      "Kalpalata Lotus": "Flowers from vines that grow on cliff sides. It is called a lotus only because it has a similar appearance to one. Aside from that, it bears no other similar properties to the lotus.",
      "Mourning Flower": "Crimson flowers that bloom on ancient battlefields. They can even flourish in the depths of the desert. Their drooping flowers seem to be in mourning for heroes long past.",
      "Nilotpala Lotus": "Growing in the forest wetlands, these plants only bloom at night with flowers as bright as the moon.",
      "Padisarah": "A holy and noble plant. The conditions for growth in its environment are very demanding. The flower buds can be processed to make valuable spices.",
      "Rukkhashava Mushrooms": "A fungus that grows in layers upon layers, like a sea of clouds, and which mostly grows on trees deep in the rainforest.",
      "Sand Grease Pupa": "You can only find such husks deep in the desert where the Quicksand Eels breed. The hardened shell is meant to protect the Quicksand Eels' larval bodies until they finally acclimate to the conditions of the dry desert.",
      "Scarab": "A tenacious beetle that finds repose within the vast ocean of desert sand. The golden pattern on such beetles' shells hints at some deep relationship between them and the ancient ruins that dot the desert.",
      "Trishiraite": "A splendorous stone that can be found in the depths of desolate mountains, seemingly formed from congealed elemental energy.",
      "Beryl Conch": "A conch-like structure that gives off a faint glow. Despite the name, it is not a shell but something condensed from pure elemental energy.",
      "Lumidouce Bell": "A serene and tranquil violet flower. It has a light, soft, and lasting scent and is often used for making luxurious perfumes.",
      "Rainbow Rose": "A delicate and tender pink flower. Despite their name, Rainbow Roses are essentially more akin to Lilies.",
      "Romaritime Flower": "An ethereal and elegant blue flower. Its tender petals are elastic and water-absorbent, making it the ideal raw material for various daily necessities."}
            
coa2_dict = {"slime-condensate": 0, "slime-secretions": 1, "slime-concentrate": 2, 
                 "damaged-mask": 0, "stained-mask": 1, "ominous-mask": 2,
                 "firm-arrowhead": 0, "sharp-arrowhead": 1, "weathered-arrowhead": 2,
                 "divining-scroll": 0, "sealed-scroll": 1, "forbidden-curse-scroll": 2,
                 "treasure-hoarder-insignia": 0, "silver-raven-insignia": 1, "golden-raven-insignia": 2,
                 "recruit's-insignia": 0, "sergeant's-insignia": 1, "lieutenant's-insignia": 2,
                 "whopperflower-nectar": 0, "shimmering-nectar": 1, "energy-nectar": 2,
                 "heavy-horn": 0, "black-bronze-horn": 1, "black-crystal-horn": 2,
                 "dead-ley-line-branch": 0, "dead-ley-line-leaves": 1, "ley-line-sprout": 2,
                 "fragile-bone-shard": 0, "sturdy-bone-shard": 1, "fossilized-bone-shard": 2,
                 "mist-grass-pollen": 0, "mist-grass": 1, "mist-grass-wick": 2,
                 "hunter's-sacrificial-knife": 0, "agent's-sacrificial-knife": 1, "inspector's-sacrificial-knife": 2,
                 "chaos-device": 0, "chaos-circuit": 1, "chaos-core": 2
    }

coa_desc = {"Slime Condensate": "A thick coating found on slimes. Most commonly seen material in elemental workshops.",
            "Slime Secretions": "Mildly purified slime secretions. Harmful to the skin. Please avoid direct exposure.", 
            "Slime Concentrate": "Concentrated slime essence. When left alone, it will begin to move on its own.",
            "Damaged Mask": "A broken bone mask that once belonged to some hilichurl. \nNow more broken than complete, it can no longer perform its primary function.",
            "Stained Mask": "A bone mask covered in unidentifiable stains, that emanates a mysterious odor.\nYet such is the devotion of hilichurls to masks that they will wear it nonetheless.",
            "Ominous Mask": "A glossy bone mask with oil markings painted on it, meant to intimidate enemies.\nNo one really knows why hilichurls are so fascinated with masks. Some say it's because they don't want to see their own reflections in the water.",
            "Firm Arrowhead": "A roughly produced arrowhead. Though unimpressive, neither it nor the bow should be underestimated, for even the bravest knight can be felled by an arrow from the rear.", 
            "Sharp Arrowhead": "A well-made arrowhead. Sharp enough to penetrate armor with the ease of a rock through the surface of water.", 
            "Weathered Arrowhead": "An old arrowhead coated in blood. The arrowhead has long since lost its sharpness and thus its use as a weapon.\nHowever it represents the pride of a hunter and acts as both an amulet and a medal.",
            "Divining Scroll": "A scroll that likely relates to some kind of magic. Exudes an inexplicable but ominous warmth.",
            "Sealed Scroll": "An old scroll lacking in detail and clarity. By following the images on it, some magical creatures can recreate a small part of its magic.",
            "Forbidden Curse Scroll": "A scroll inscribed with ancient images. It is said that few can decipher its meaning, and the few scholars that have all went mad.", 
            "Treasure Hoarder Insignia": "A signet that proudly represents its owner's position as a member of the Treasure Hoarders. The pursuit of treasure knows no bounds. That said... is being a thief something to be proud of?", 
            "Silver Raven Insignia": "A raven insignia used by members of the Treasure Hoarders to identify each other. The Treasure Hoarders ask for no resume. Anyone who has an insatiable desire for treasure and is backed up by an equal amount of courage can become a worthy member.", 
            "Golden Raven Insignia": "A raven insignia that symbolizes the pride and the guiding principle of the Treasure Hoarders. Whether it's hidden amidst the vastness of the land or in the depths of the seas, as long as there are treasures to be hunted down, the spirit of Treasure Hoarders, who will stop at nothing to acquire them, will never die.", 
            "Recruit's Insignia": "An insignia to identify the recruits. Makes one wonder about what the ones joining the Fatui's war machine were thinking.",
            "Sergeant's Insignia": "An insignia with a different shape to distinguish the sergeants from new recruits. Perhaps there are complicated emotions behind it.",
            "Lieutenant's Insignia": "An insignia to identify officers. The Fatui possess a colossal army, so there must be something extraordinary about the ones who achieved this rank within the group.", 
            "Whopperflower Nectar": "Nectar extracted from the stamen of a Whopperflower that contains trace amounts of elemental energy. The taste of the nectar has a hint of Sweet Flower in it.", 
            "Shimmering Nectar": "Nectar that is full of pure elemental energy.\nScholars generally concur that Whopperflowers are advanced life forms among the elemental plants, but there has yet to be a satisfactory explanation regarding their predatory habits.",
            "Energy Nectar": "A thick and sticky honey that is full of energy. The Whopperflower hunts by tricking its prey, a process it uses to possibly evolve into a more powerful and pure form.",
            "Heavy Horn": "A crude horn used by hilichurls to warn each other. Given the damage to the horn, it won't be warning anyone any time soon.",
            "Black Bronze Horn": "A metallic monster horn that can only be obtained from especially strong hilichurls, since blowing on the horn takes real strength.", 
            "Black Crystal Horn": "A metallic horn with an ominous shine decorated with black crystals of an unknown source. It has hardly been used at all. It is likely a ceremonial item of the hilichurls'.",
            "Dead Ley Line Branch": "Fragile branches from deep within the earth. Even after years of aging, from beneath it's mottled surface you can see that its power is not yet entirely lost.",
            "Dead Ley Line Leaves": "A twig from deep within the earth. Though it is far from where it once lay, its leaves still pulsate with energy.",
            "Ley Line Sprout": "It is said that there was a great tree whose roots once spread out to every corner of the world, and this branch is said to be part of it. It is almost if it was never broken off and taken far away, for its vitality is such that it still sprouts new leaves even now.", 
            "Fragile Bone Shard": "A bone shard once carried by a Geovishap. \nAlthough they are quite fragile, they seem to still harbor some indescribable power.", 
            "Sturdy Bone Shard": "A fragment of an unknown creature's bones that appear to be prized by Geovishaps for some reason.\nThe fragment appears to be quite aged. Despite being dragon-like beasts with no spoken language, they still seem to have some sort of special affection for these bone shards.",
            "Fossilized Bone Shard": "A fossilized bone fragment sometimes found after defeating Geovishaps.\nGeovishaps all dream of growing into great dragons one day. They see these fossils as dragon bones and greatly cherish them, perhaps because they too hope to attain the dragons' longevity and power.",
            "Mist Grass Pollen": "Strange spores created by Mist Grass in enclosed spaces. They are the Cicins' favorite food.", 
            "Mist Grass": "Well-preserved Mist Grass. Some would take advantage of the Cicins' love for the Mist Grass to control them.", 
            "Mist Grass Wick": "A rare bundle of Mist Grass that gives off a faint glow. Those who carry it invite both the Cicins and misfortune.",
            "Hunter's Sacrificial Knife": "A sharp alloy weapon. Though its owner has been lost, it still reflects a disturbingly cold light.", 
            "Agent's Sacrificial Knife": "An oddly-shaped weapon made with superior Snezhnayan technology that once belonged to a senior agent. Proper training is required for using this strange weapon.",
            "Inspector's Sacrificial Knife": "In the hands of its lord, this fierce weapon has handled many \"debts.\" No one has eyes in the back of their heads, and this weapon and its related techniques are designed around that weakness.",
            "Chaos Device": "Comes from ancient defunct relic structures. A part that once held the structure together. Its aesthetically-pleasing engineering is quite exquisite.",
            "Chaos Circuit": "Comes from ancient defunct relic structures. Was once a logic circuit responsible for movement functions. Sadly, no one is able to make sense of how it worked.",
            "Chaos Core": "Comes from ancient defunct relic structures. The core that once drove a mechanical beast. Should you come to understand its workings and reproduce it, you could perhaps change the world."  
}

tb = {"teachings-of-freedom": 0,
      "guide-to-freedom": 1,
      "philosophies-of-freedom": 2,
      "teachings-of-resistance": 0,
      "guide-to-resistance": 1,
      "philosophies-of-resistance": 2,
      "teachings-of-ballad": 0,
      "guide-to-ballad": 1,
      "philosophies-of-ballad": 2,
      "teachings-of-prosperity": 0,
      "guide-to-prosperity": 1,
      "philosophies-of-prosperity": 2,
      "teachings-of-diligence": 0,
      "guide-to-diligence": 1,
      "philosophies-of-diligence": 2,
      "teachings-of-gold": 0,
      "guide-to-gold": 1,
      "philosophies-of-gold": 2,
      "teachings-of-transience": 0,
      "guide-to-transience": 1,
      "philosophies-of-transience": 2,
      "teachings-of-elegance": 0,
      "guide-to-elegance": 1,
      "philosophies-of-elegance": 2,
      "teachings-of-light": 0,
      "guide-to-light": 1,
      "philosophies-of-light": 2,
      "teachings-of-admonition": 0,
      "guide-to-admonition": 1,
      "philosophies-of-admonition": 2,
      "teachings-of-ingenuity": 0,
      "guide-to-ingenuity": 1,
      "philosophies-of-ingenuity": 2,
      "teachings-of-praxis": 0,
      "guide-to-praxis": 1,
      "philosophies-of-praxis": 2,
      "teachings-of-equity": 0,
      "guide-to-equity": 1,
      "philosophies-of-equity": 2,
      "teachings-of-justice": 0,
      "guide-to-justice": 1,
      "philosophies-of-justice": 2,
      "teachings-of-order": 0,
      "guide-to-order": 1,
      "philosophies-of-order": 2}

tb_desc = {"teachings-of-freedom": "Talent Level-Up material.\nFreedom is the spirit of the land of the wind.\nThe freedom to live is one of such. It is the freedom to live freely and healthily without concerns of one's own safety.",
      "guide-to-freedom": "Talent Level-Up material.\nFreedom is the spirit of the land of the wind.\nThe freedom of travel is one of such. It is the freedom to traverse the land freely without being obstructed.",
      "philosophies-of-freedom": "Talent Level-Up material.\nFreedom is the spirit of the land of the wind.\nTo sing is one such freedom. To sing on the land created by the Anemo Archon is to send your heart away with the song on the wind.",
      "teachings-of-resistance": "Talent Level-Up material.\nResistance is the backbone of the land of the wind.\nThe history of Mondstadt is one of resistances. People rose up to prevent past conflicts from ever being forgotten, like sprouts breaking through the soil, like the eternal wind eroding through stone walls.",
      "guide-to-resistance": "Talent Level-Up material.\nResistance is the backbone of the city of Wind.\nThe history of Mondstadt is one of resistances. People rose up to grant the citizens of Mondstadt the freedom they now enjoy, like the Anemo Archon blowing away the snow, or like Vennessa rising up to fight.",
      "philosophies-of-resistance": "Talent Level-Up material.\nResistance is the backbone of the land of the wind.\nThe history of Mondstadt is one of resistances. People rose up to allow the future Mondstadt's poetry to freely be that of the wind and be spread across the land.",
      "teachings-of-ballad": "Talent Level-Up material.\nPoetry is the soul of the land of the wind.\nPoetry is the manifestations of beautiful feelings. On a beautiful day, the breezes carry with them poetry that touches the heart of people like the wind caressing the leaves.",
      "guide-to-ballad": "Talent Level-Up material.\nPoetry is the soul of the land of the wind.\nPoetry is the manifestations of the will to encourage. In the dark days, the gales in the streets and alleyways whisper words of fury, like the battle drums, like the low rumbling before the storm.",
      "philosophies-of-ballad": "Talent Level-Up material.\nPoetry is the soul of the land of the wind.\nPoetry is the manifestations of the desire to spread the word. Though nothing is eternal, though nothing will be the same, the wind's poetry will still spread beyond the skies, the land, the seas to every corner of the world.",
      "teachings-of-prosperity": "Talent Level-Up material.\nProsperity is the people's pursuit in the land of Geo.\nProsperity is the blessing of Liyue, it is the foundation of the great city built by the gods and the people of Liyue, and it is the source of the peace and safety of the land.",
      "guide-to-prosperity": "Talent Level-Up material.\nProsperity is the people's pursuit in the land of Geo.\nProsperity is the promise made by Liyue to its children: To repay the hard-working laborers with enough gold to brighten up this land.",
      "philosophies-of-prosperity": "Talent Level-Up material.\nProsperity is the people's pursuit in the land of Geo.\nProsperity is Liyue's past, present, and future. This prosperity is unmatched and unobtainable by any other nations — it all belongs to Liyue and its inhabitants.",
      "teachings-of-diligence": "Talent Level-Up material.\nIndustriousness is the foundation of the land of Geo.\nDiligence is having the bravery and the strength to conquer mountains and seas and to pursue gold and prosperity through honest, hard work.",
      "guide-to-diligence": "Talent Level-Up material.\nIndustriousness is the foundation of the land of Geo.\nIndustriousness is the catalyst that flows in the blood of the people of Liyue, able to turn rocks into gold. It is what lies behind the greatness of its great commercial port.",
      "philosophies-of-diligence": "Talent Level-Up material.\nIndustriousness is the foundation of the land of Geo.\nIndustriousness is believing in one's own ability to earn a place in the land of the gods through sweat, wisdom, and power.",
      "teachings-of-gold": "Talent Level-Up material.\nGold is the symbol of the land of Geo.\nGold is the blood that flows deep within Liyue's veins, the muscle that makes up Liyue's beating heart, and the bones that make Liyue stand proud.",
      "guide-to-gold": "Talent Level-Up material.\nGold is the symbol of the land of Geo.\nGold symbolizes conversion. This is the unspoken understanding between Liyue's mountains, land, city, and people. In Liyue, industriousness is converted into gold, and gold into prosperity.",
      "philosophies-of-gold": "Talent Level-Up material.\nGold is the symbol of the land of Geo.\nGold is the wealth of Liyue, but Liyue's true wealth is the hearts of its people that shine like gold.",
      "teachings-of-transience": "Talent Level-Up material.\nTransience is the dream of the nation of thunder.\nFleeting glories are the highest expression of mortal beauty, for are we mortals not like the flashing lightning itself? Like a lovely dream or blossoming spark, we shall leave a gorgeous mark on the eternal night sky.",
      "guide-to-transience": "Talent Level-Up material.\nTransience is the dream of the nation of thunder.\nWe find the greatest joys in mortal life in transient dreams, for is life itself not like the shadow of the thunder? Pursue your dreams into the clouds if you wish, and enjoy the unexpected silence of the dim lamp-lit nights.",
      "philosophies-of-transience": "Talent Level-Up material.\nTransience is the dream of the nation of thunder.\nThe fleeting nature of this mortal world is the essence of beauty, for are our lives in this world not akin to the levin flash? Yet the might of the divine comes suddenly, and before the roar of eternity, who can stand?",
      "teachings-of-elegance": "Talent Level-Up material.\nElegance is the form of the nation of thunder.\nElegance brooks no flattery, and the elegant are ever noble. They are like the sea eagles who soar on high to contend with the resounding storms. They will not cater to philistine vulgarity, as one would not cast a flower crown into the mud, staining its dignity.",
      "guide-to-elegance": "Talent Level-Up material.\nElegance is the form of the nation of thunder.\nElegance shuns arrogance. The elegant are ever humble, and only by discarding vanity and sloth may one see clearly — and is there not beauty and loveliness even in the basest of appearances?",
      "philosophies-of-elegance": "Talent Level-Up material.\nElegance is the form of the nation of thunder.\nElegance abhors vulgarity, and the elegant ever walk alone. Resisting base evils, unmoved by base loves, never taking refuge in base ignorance — that is how one perceives the chasm between the elegant and the contemptuous.",
      "teachings-of-light": "Talent Level-Up material.\nLight is the yearning of the land of thunder.\nThe ruler who claims to have perceived all forever aims to hoard celestial glory. But this vision that cannot be shared only leads people to long for it more fiercely, like moths diving into the flame.",
      "guide-to-light": "Talent Level-Up material.\nLight is the yearning of the land of thunder.\nThough the sun rays themselves should be blocked by layers upon layers of clouds, there are still those in the thunder god's land who dream of piercing that wrathful sea of lightning to pursue the glory of the divine, fearing not that they shall be cruelly struck down.",
      "philosophies-of-light": "Talent Level-Up material.\nLight is the yearning of the land of thunder.\nThough they must live forever on the earth, humanity will always reach for the light. Mortals will pursue and surpass, and they will never stop. A sealed eternity may, perhaps, look magnificent, but its essence is death.",
      "teachings-of-admonition": "Talent Level-Up material.\nAdmonition is the branches of the nation of wisdom.\nAdmonition comes from a pure heart. Only sensible words of goodwill can express profound wisdom and free the sprout of knowledge from the shackles of arrogance.",
      "guide-to-admonition": "Talent Level-Up material.\nAdmonition is the branches of the nation of wisdom.\nAdmonition is paired with wise thinking. Careful deliberation affords humble words a clarity that convinces the wise and enlightens the foolish. Such words allow wisdom to flow like an unobstructed river.",
      "philosophies-of-admonition": "Talent Level-Up material.\nAdmonition is the branches of the nation of wisdom.\nAdmonition is completed by good deeds. What is done confers real meaning upon what is said. When one's mind, words, and deeds are aligned, their nourishment shall guarantee the fruition of wisdom's tree.",
      "teachings-of-ingenuity": "Talent Level-Up material.\nIngenuity is the leaf-veins of the nation of wisdom.\nIngenuity springs forth from benevolent consideration. They say that \"a poisonous tree bears no kind fruit.\" Similarly, ingenious nascent ideas are always born from determined and benign minds, for only they are worthy bearers of wisdom.",
      "guide-to-ingenuity": "Talent Level-Up material.\nIngenuity is the leaf-veins of the nation of wisdom. Ingenuity sets words of integrity on the right path. One who thinks out of goodwill and in a clever and careful fashion never deviates from the path of boons. Yet one who thinks with contempt and malice shall taint their words with despicable colors.",
      "philosophies-of-ingenuity": "Talent Level-Up material.\nIngenuity is the leaf-veins of the nation of wisdom.\nIngenuity is completed by harmonious conduct. What is done completes what is thought. Wisdom blooms where the mind, words, and practice converge.",
      "teachings-of-praxis": "Talent Level-Up material.\nPraxes are the roots of the nation of wisdom.\nPraxes stem from an unwavering will. All wisdom is manifested through the unyielding pursuit of goodness. Where goodness is not practiced, ingenuity and eloquence wither.",
      "guide-to-praxis": "Talent Level-Up material.\nPraxes are the roots of the nation of wisdom.\nPraxes validate words of honesty. Though one speaks and acts out of goodwill, one has not yet obtained wisdom. Wisdom, born from action, is a signet pressed upon honest words.",
      "philosophies-of-praxis": "Talent Level-Up material.\nPraxes are the roots of the nation of wisdom.\nPraxes bring forth the fruit of wisdom. Practice grants itself meaning, and it is only by treading a path that unites action, speech, and thought that the wise may reach perfection.",
      "teachings-of-equity": "Talent Level-Up material.\nThe shore of the Nation of Water is equity.\nEquity sets boundaries on rights. Without equity, the rights granted by law will be abused, and become a tool to damage our virtuous customs.",
      "guide-to-equity": "Talent Level-Up material.\nThe shore of the Nation of Water is equity.\nEquity is the foundation upon which Fontaine was founded. Equity forms the standard of the law. If law loses the essence of equity, it will become a chessboard played for profit.",
      "philosophies-of-equity": "Talent Level-Up material.\nThe shore of the Nation of Water is equity.\nEquity is the foundation upon which Fontaine was founded. Equity requires the continuous and steady support of morality and law, and morality and law constantly change based upon the invariant principle of equity.",
      "teachings-of-justice": "Talent Level-Up material.\nThe sword of the Nation of Water is justice.\nThe law of Fontaine walks with the sword of justice in hand. Without the guidance of justice, all law is reduced to meaningless words, to be tampered with and slaughtered at a whim.",
      "guide-to-justice": "Talent Level-Up material.\nThe sword of the Nation of Water is justice.\nThe law of Fontaine walks with the sword of justice in hand. Justice must be blind, and those who wield the sword of justice must not be led astray by their own interests or affairs.",
      "philosophies-of-justice": "Talent Level-Up material.\nThe sword of the Nation of Water is justice.\nThe law of Fontaine walks with the sword of justice in hand. Justice means judgment and reconciliation, the blade of judgment arrests the actions of evil, while reconciliation maintains order.",
      "teachings-of-order": "Talent Level-Up material.\nThe shield of the Nation of Water is order.\nAll law in Fontaine ultimately serves to maintain a stable order. Without order, there is chaos, and there can be no fairness in chaos.",
      "guide-to-order": "Talent Level-Up material.\nThe shield of the Nation of Water is order.\nAll law in Fontaine ultimately serves to maintain a stable order. Without the guarantee provided by order, justice will be reduced to unlimited violence, a weapon used by all against all.",
      "philosophies-of-order": "Talent Level-Up material.\nThe shield of the Nation of Water is order.\nAll law in Fontaine ultimately serves to maintain a stable order. Equity and justice come from order, and serve order. Like the still, ripple-less surface of the waters of Fontaine, order is the cornerstone of Fontaine's existence."}




#"ci": {}
#"ls": {}
#"tbk": {}
#"tbs": {}
#"wa": {}
#"we": {}