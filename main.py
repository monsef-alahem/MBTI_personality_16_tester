'''
author  :   monsef alahem
email   :   m.alahem09@gmail.com
version :   1.0
start   :   09-13-2021
'''

import os

main_index = 0
answer_tab = [0]*70
personality = 'AAAA'


personality_tab = [
#1
"Portrait of an ENFJ - Extraverted iNtuitive Feeling Judging (Extraverted Feeling with Introverted Intuition)\n\
												The Giver\n\
\n\
ENFJs have a special gift with people, and are basically happy people when they can use that gift to help others.\n\
They get their best satisfaction from serving others. Their genuine interest in Humankind and their exceptional\n\
intuitive awareness of people makes them able to draw out even the most reserved individuals. ENFJs have a strong\n\
need for close, intimate relationships, and will put forth a lot of effort in creating and maintaining these relationships.\n\
They're very loyal and trustworthy once involved in a relationship.\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Extraverted Feeling\n\
	Auxiliary: Introverted Intuition\n\
	Tertiary: Extraverted Sensing\n\
	Inferior: Introverted Thinking\n\
\n\
ENFJs generally have the following traits:\n\
	o Genuinely and warmly interested in people\n\
	o Value people's feelings\n\
	o Value structure and organization\n\
	o Value harmony, and good at creating it\n\
	o Exceptionally good people skills\n\
	o Dislike impersonal logic and analysis\n\
	o Strong organizational capabilities\n\
	o Loyal and honest\n\
	o Creative and imaginative\n\
	o Enjoy variety and new challenges\n\
	o Get personal satisfaction from helping others\n\
	o Extremely sensitive to criticism and discord\n\
	o Need approval from others to feel good about themselves\n"
,#2
"Portrait of an ENTJ - Extraverted iNtuitive Thinking Judging (Extraverted Thinking with Introverted Intuition)\n\
													The Executive\n\
\n\
ENTJ's are natural born leaders. They live in a world of possibilities where they see all sorts of challenges to be\n\
surmounted, and they want to be the ones responsible for surmounting them. They have a drive for leadership, which\n\
is well-served by their quickness to grasp complexities, their ability to absorb a large amount of impersonal information\n\
, and their quick and decisive judgments. They are \"take charge\" people.\n\
\n\
ENTJ’s love to interact with people. As Extroverts, they're energized and stimulated primarily externally. There's nothing\n\
more enjoyable and satisfying to the ENTJ than having a lively, challenging conversation. They especially respect people\n\
who are able to stand up to the ENTJ, and argue persuasively for their point of view. There aren't too many people who will\n\
do so, however, because the ENTJ is a very forceful and dynamic presence who has a tremendous amount of self-confidence and\n\
excellent verbal communication skills. Even the most confident individuals may experience moments of self-doubt when debating\n\
a point with an ENTJ.\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Extraverted Thinking\n\
	Auxiliary: Introverted Intuition\n\
	Tertiary: Extraverted Sensing\n\
	Inferior: Introverted Feeling\n\
\n\
ENTJ’s generally have the following traits:\n\
	o Driven to turn theories into plans\n\
	o Highly value knowledge\n\
	o Future-oriented\n\
	o Natural leaders\n\
	o Impatient with inefficiency and incompetence\n\
	o Want things structured and orderly\n\
	o Excellent verbal communication skills\n\
	o Dislike routine, detail-oriented tasks\n\
	o Self-confident\n\
	o Decisive\n\
"
,#3
"Portrait of an ENFP - Extraverted iNtuitive Feeling Perceiving (Extraverted Intuition with Introverted Feeling)\n\
														The Inspirer\n\
\n\
ENFPs are warm, enthusiastic people, typically very bright and full of potential. They live in the world of\n\
possibilities, and can become very passionate and excited about things. Their enthusiasm lends them the ability\n\
to inspire and motivate others, more so than we see in other types. They can talk their way in or out of anything.\n\
They love life, seeing it as a special gift, and strive to make the most out of it.Project-oriented, they may go\n\
through several different careers during their lifetime.\n\
\n\
ENFPs are basically happy people. They may become unhappy when they are confined to strict schedules or mundane tasks.\n\
Consequently, ENFPs work best in situations where they have a lot of flexibility, and where they can work with people\n\
and ideas. Many go into business for themselves. They have the ability to be quite productive with little supervision,\n\
as long as they are excited about what they're doing.\n\
\n\
Because they are so alert and sensitive, constantly scanning their environments, ENFPs often suffer from muscle tension.\n\
They have a strong need to be independent, and resist being controlled or labeled. They need to maintain control over\n\
themselves, but they do not believe in controlling others. Their dislike of dependence and suppression extends to others\n\
as well as to themselves.\n\
\n\
ENFPs are charming, ingenuous, risk-taking, sensitive, people-oriented individuals with capabilities ranging across a broad\n\
spectrum. They have many gifts which they will use to fulfill themselves and those near them.\n\
\n\
Jungian functional preference ordering for ENFP:\n\
	Dominant: Extraverted Intuition\n\
	Auxiliary: Introverted Feeling\n\
	Tertiary: Extraverted Thinking\n\
	Inferior: Introverted Sensing\n\
\n\
ENFPs generally have the following traits:\n\
	o Project-oriented\n\
	o Bright and capable\n\
	o Warmly, genuinely interested in people; great people skills\n\
	o Extremely intuitive and perceptive about people\n\
	o Able to relate to people on their own level\n\
	o Service-oriented; likely to put the needs of others above their own\n\
	o Future-oriented\n\
	o Dislike performing routine tasks\n\
	o Need approval and appreciation from others\n\
	o Cooperative and friendly\n\
	o Creative and energetic\n\
	o Well-developed verbal and written communication skills\n\
	o Natural leaders, but do not like to control people\n\
	o Resist being controlled by others\n\
	o Can work logically and rationally - use their intuition to understand the goal and work backwards\n\
	towards it\n\
	o Usually able to grasp difficult concepts and theories\n\
"
,#4
"Portrait of an ENTP - Extraverted iNtuitive Thinking Perceiving (Extraverted Intuition with Introverted Thinking)\n\
													The Visionary\n\
\n\
As an ENTP, your primary mode of living is focused externally, where you take things in primarily via your\n\
intuition. Your secondary mode is internal, where you deal with things rationally and logically.\n\
With Extraverted Intuition dominating their personality, the ENTP's primary interest in life is understanding\n\
the world that they live in. Using their intuition to process this information, they are usually extremely\n\
quick and accurate in their ability to size up a situation. With the exception of their ENFP cousin,\n\
the ENTP has a deeper understanding of their environment than any of the other types.\n\
\n\
This ability to intuitively understand people and situations puts the ENTP at a distinct advantage in their lives.\n\
Accordingly, they are quite flexible and adapt well to a wide range of tasks, they are also resourceful when solving problems.\n\
\n\
ENTP's are idea people. Their perceptive abilities cause them to see possibilities everywhere. They get excited\n\
and enthusiastic about their ideas, and are able to spread their enthusiasm to others. In this way, they get the\n\
support that they need to fulfill their visions.\n\
\n\
Jungian functional preference ordering for ENTP:\n\
	Dominant: Extraverted Intuition\n\
	Auxiliary: Introverted Thinking\n\
	Tertiary: Extraverted Feeling\n\
	Inferior: Introverted Sensing\n\
\n\
ENTP’s generally have the following traits:\n\
	o Project-oriented\n\
	o Enjoy generating ideas and theories\n\
	o Creative and ingenious\n\
	o Bright and capable\n\
	o Flexible and Diverse\n\
	o Excellent communication skills\n\
	o Enjoy debating issues with other people\n\
	o Excellent people skills\n\
	o Natural leaders, but do not like to control people\n\
	o Resist being controlled by people\n\
	o Lively and energetic; able to motivate others\n\
	o Highly value knowledge and competence\n\
	o Logical, rational thinkers\n\
	o Able to grasp difficult concepts and theories\n\
	o Enjoy solving difficult problems\n\
	o Dislike confining schedules and environments\n\
	o Dislike routine, detailed tasks\n\
"
,#5
"Portrait of an ESFJ - Extraverted Sensing Feeling Judging (Extraverted Feeling with Introverted Sensing)\n\
												The Caregiver\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Extraverted Feeling\n\
	Auxiliary: Introverted Sensing\n\
	Tertiary: Extraverted Intuition\n\
	Inferior: Introverted Thinking\n\
\n\
ESFJ’s generally have the following traits:\n\
	o Organized\n\
	o Loyal\n\
	o Can be depended on to follow things through to completion\n\
	o Enjoy creating order, structure and schedules\n\
	o Enjoy interacting with people\n\
	o Warm-hearted and sympathetic\n\
	o Tend to put others' needs above their own\n\
	o Very good at giving practical care\n\
	o Very cooperative, good team members\n\
	o Practical and down-to-earth\n\
	o Value peaceful living and security\n\
	o Enjoy variety, but work well with routine tasks\n\
	o Need approval from others\n\
	o Receive satisfaction from giving to others\n\
	o Live in the here and now - dislike theorizing about the future\n\
"
,#6
"Portrait of an ESFP - Extraverted Sensing Feeling Perceiving (Extraverted Sensing with Introverted Feeling)\n\
												The Performer\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Extraverted Sensing\n\
	Auxiliary: Introverted Feeling\n\
	Tertiary: Extraverted Thinking\n\
	Inferior: Introverted Intuition\n\
\n\
ESFP’s generally have the following traits:\n\
	o Live in the present moment\n\
	o Are stimulated and excited by new experiences\n\
	o Practical and realistic\n\
	o Warmly interested in people\n\
	o Know how to have a good time, and how to make things fun for others\n\
	o Independent and resourceful\n\
	o Spontaneous - seldom plan ahead\n\
	o Hate structure and routine\n\
	o Dislike theory and long written explanations\n\
	o Feel special bond with children and animals\n\
	o Strongly developed aesthetic appreciation for things\n\
	o Great people skills\n\
"
,
#7
"Portrait of an ESTJ - Extraverted Sensing Thinking Judging (Extraverted Thinking with Introverted Sensing)\n\
												The Guardian\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Extraverted Thinking\n\
	Auxiliary: Introverted Sensing\n\
	Tertiary: Extraverted Intuition\n\
	Inferior: Introverted Feeling\n\
\n\
ESTJ’s generally have the following traits:\n\
	o Natural leaders - they like to be in charge\n\
	o Value security and tradition\n\
	o Loyal\n\
	o Hard-working and dependable\n\
	o Athletic and wholesome\n\
	o Have a clear set of standards and beliefs which they live by\n\
	o No patience with incompetence or inefficiency\n\
	o Excellent organizational abilities\n\
	o Enjoy creating order and structure\n\
	o Very thorough\n\
	o Will follow projects through to completion\n\
	o Straight-forward and honest\n\
	o Driven to fulfill their duties\n\
"
,#8
"Portrait of an ESTP - Extraverted Sensing Thinking Perceiving (Extraverted Sensing with Introverted Thinking)\n\
													The Doer\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Extraverted Sensing\n\
	Auxiliary: Introverted Thinking\n\
	Tertiary: Extraverted Feeling\n\
	Inferior: Introverted Intuition\n\
\n\
ESTP’s generally have the following traits:\n\
	o Action-oriented\n\
	o Live in the present moment\n\
	o Dislike abstract theory without practical application\n\
	o Like to see immediate results for their efforts\n\
	o Fast-paced and energetic\n\
	o Flexible and adaptable\n\
	o Resourceful\n\
	o Seldom work from a plan - make things up as they go\n\
	o Fun to be around\n\
	o Highly observant\n\
	o Excellent memory for details\n\
	o Excellent people skills\n\
	o Good-natured\n\
	o Excellent ability to see an immediate problem and quickly devise a solution\n\
	o Attracted to adventure and risk\n\
	o May be flashy or showy\n\
	o Like initiating things - not necessarily following them through to completion\n\
"
,#9
"Portrait of an INFJ Introverted iNtuitive Feeling Judging (Introverted Intuition with Extraverted Feeling)\n\
												The Protector\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Intuition\n\
	Auxiliary: Extraverted Feeling\n\
	Tertiary: Introverted Thinking\n\
	Inferior: Extraverted Sensing\n\
\n\
INFJ’s generally have the following traits:\n\
	o Intuitively understand people and situations\n\
	o Idealistic\n\
	o Highly principled\n\
	o Complex and deep\n\
	o Natural leaders\n\
	o Sensitive and compassionate towards people\n\
	o Service-oriented\n\
	o Future-oriented\n\
	o Value deep, authentic relationships\n\
	o Reserved about expressing their true selves\n\
	o Dislike dealing with details unless they enhance or promote their vision\n\
	o Constantly seeking meaning and purpose in everything\n\
	o Creative and visionary\n\
	o Intense and tightly-wound\n\
	o Can work logically and rationally - use their intuition to understand the goal and work backwards\n\
	towards it\n\
"
,#10
"Portrait of an INFP - Introverted iNtuitive Feeling Perceiving (Introverted Feeling with Extraverted Intuition)\n\
														The Idealist\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Feeling\n\
	Auxiliary: Extraverted Intuition\n\
	Tertiary: Introverted Sensing\n\
	Inferior: Extraverted Thinking\n\
\n\
INFP’s generally have the following traits:\n\
	o Strong value systems\n\
	o Warmly interested in people\n\
	o Service-oriented, usually putting the needs of others above their own\n\
	o Loyal and devoted to people and causes\n\
	o Future-oriented\n\
	o Growth-oriented; always want to be growing in a positive direction\n\
	o Creative and inspirational\n\
	o Flexible and laid-back, unless a ruling principle is violated\n\
	o Sensitive and complex\n\
	o Dislike dealing with details and routine work\n\
	o Original and individualistic - \"out of the mainstream\"\n\
	o Excellent written communication skills\n\
	o Prefer to work alone, and may have problems working on teams\n\
	o Value deep and authentic relationships\n\
	o Want to be seen and appreciated for who they are\n\
"
,#11
"Portrait of an INTJ Introverted iNtuitive Thinking Judging (Introverted Intuition with Extraverted Thinking)\n\
												The Scientist\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Intuition\n\
	Auxiliary: Extraverted Thinking\n\
	Tertiary: Introverted Feeling\n\
	Inferior: Extraverted Sensing\n\
\n\
INTJ’s generally have the following traits:\n\
	o Able to absorb extremely complex theoretical and complex material\n\
	o Driven to create order and structure from theoretical abstractions\n\
	o Supreme strategists\n\
	o Future-oriented\n\
	o See the global, \"big picture\"\n\
	o Strong insights and intuitions, which they trust implicitly\n\
	o Value their own opinions over others\n\
	o Love difficult theoretical challenges\n\
	o Bored when dealing with mundane routine\n\
	o Value knowledge and efficiency\n\
	o Have no patience with inefficiency and confusion\n\
	o Have very high standards for performance, which they apply to themselves most\n\
	strongly\n\
	o Reserved and detached from others\n\
	o Calm, collected and analytical\n\
	o Extremely logical and rational\n\
	o Original and independent\n\
	o Natural leaders, but will follow those they can fully support\n\
	o Creative, ingenious, innovative, and resourceful\n\
	o Work best alone, and prefer to work alone\n\
"
,#12
"Portrait of an INTP Introverted iNtuitive Thinking Perceiving (Introverted Thinking with Extraverted Intuition)\n\
														The Thinker\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Thinking\n\
	Auxiliary: Extraverted Intuition\n\
	Tertiary: Introverted Sensing\n\
	Inferior: Extraverted Feeling\n\
\n\
INTP’s generally have the following traits:\n\
	o Love theory and abstract ideas\n\
	o Truth Seekers - they want to understand things by analyzing underlying principles and structures\n\
	o Value knowledge and competence above all else\n\
	o Have very high standards for performance, which they apply to themselves\n\
	o Independent and original, possibly eccentric\n\
	o Work best alone, and value autonomy\n\
	o Have no desire to lead or follow\n\
	o Dislike mundane detail\n\
	o Not particularly interested in the practical application of their work\n\
	o Creative and insightful\n\
	o Future-oriented\n\
	o Usually brilliant and ingenious\n\
	o Trust their own insights and opinions above others\n\
	o Live primarily inside their own minds, and may appear to be detached and\n\
	uninvolved with other people\n\
"
,#13
"Portrait of an ISFJ Introverted Sensing Feeling Judging (Introverted Sensing with Extraverted Feeling)\n\
												The Nurturer\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Sensing\n\
	Auxiliary: Extraverted Feeling\n\
	Tertiary: Introverted Thinking\n\
	Inferior: Extraverted Intuition\n\
\n\
ISFJ’s generally have the following traits:\n\
	o Large, rich inner store of information which they gather about people\n\
	o Highly observant and aware of people's feelings and reactions\n\
	o Excellent memory for details which are important to them\n\
	o Very in-tune with their surroundings - excellent sense of space and function\n\
	o Can be depended on to follow things through to completion\n\
	o Will work long and hard to see that jobs get done\n\
	o Stable, practical, down-to-earth - they dislike working with theory and abstract\n\
	thought\n\
	o Dislike doing things which don't make sense to them\n\
	o Value security, tradition, and peaceful living\n\
	o Service-oriented: focused on what people need and want\n\
	o Kind and considerate\n\
	o Likely to put others' needs above their own\n\
	o Learn best with hands-on training\n\
	o Enjoy creating structure and order\n\
	o Take their responsibilities seriously\n\
	o Extremely uncomfortable with conflict and confrontation\n\
"
,#14
"Portrait of an ISFP - Introverted Sensing Feeling Perceiving (Introverted Feeling with Extraverted Sensing)\n\
													The Artist\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Feeling\n\
	Auxiliary: Extraverted Sensing\n\
	Tertiary: Introverted Intuition\n\
	Inferior: Extraverted Thinking\n\
\n\
ISFP’s generally have the following traits:\n\
	o Keen awareness of their environment\n\
	o Live in the present moment\n\
	o Enjoy a slower pace - they like to take time to savor the present moment\n\
	o Dislike dealing with theory or abstract thought, unless they see a practical\n\
	application\n\
	o Faithful and loyal to people and ideas which are important to them\n\
	o Individualistic, having no desire to lead or follow\n\
	o Take things seriously, although they frequently appear not to\n\
	o Special bond with children and animals\n\
	o Quiet and reserved, except with people they know extremely well\n\
	o Trusting, sensitive, and kind\n\
	o Service-oriented; they're driven to help others\n\
	o Extremely well-developed appreciation for aesthetic beauty\n\
	o Likely to be original and unconventional\n\
	o Learn best with hands-on training\n\
	o Hate being confined to strict schedules and regimens\n\
"
,#15
"Portrait of an ISTJ - Introverted Sensing Thinking Judging (Introverted Sensing with Extraverted Thinking)\n\
											The Duty Fulfiller\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Sensing\n\
	Auxiliary: Extraverted Thinking\n\
	Tertiary: Introverted Feeling\n\
	Inferior: Extraverted Intuition\n\
\n\
ISTJ’s generally have the following traits:\n\
	o Value tradition, security, and peaceful living\n\
	o Will work long and hard to fulfill duties\n\
	o Can be depended on to follow through on tasks\n\
	o Loyal and faithful\n\
	o Stable, practical and down-to-earth\n\
	o Family-minded\n\
	o Dislike doing things which don't make sense to them\n\
	o Dislike abstract theory, unless they see the practical application\n\
	o Natural leaders\n\
	o Prefer to work alone, but work well in teams when necessary\n\
	o Extremely observant, they take in facts via their senses and store them internally\n\
	o Vast, rich inner store of facts which they rely on to understand problems which\n\
	they encounter in their lives\n\
	o Profound respect for facts and concrete information\n\
	o Make decisions objectively, applying logic and rational thinking\n\
	o Dislike change, unless they are shown it's benefit in a concrete way\n\
	o Have strong opinions about the way things should be done\n\
	o Appreciate structured, orderly environments\n\
	o Have very high standards for their own behavior and the behavior of others\n\
	o Not naturally in-tune with other people's feelings\n\
	o Able to accomplish almost anything if they put their minds to it\n\
	o Community minded \"good citizens\"\n\
"
,#16
"Portrait of an ISTP Introverted Sensing Thinking Perceiving (Introverted Thinking with Extraverted Sensing)\n\
													The Mechanic\n\
\n\
Jungian functional preference ordering:\n\
	Dominant: Introverted Thinking\n\
	Auxiliary: Extraverted Sensing\n\
	Tertiary: Introverted Intuition\n\
	Inferior: Extraverted Feeling\n\
\n\
ISTP’s generally have the following traits:\n\
	o Interested in how and why things work\n\
	o Do not function well in regimented, structured environments; they will either feel\n\
	stifled or become intensely bored\n\
	o Constantly gather facts about their environment and store them away\n\
	o Have an excellent ability to apply logic and reason to their immense store of facts\n\
	to solve problems or discover how things work\n\
	o Learn best \"hands-on\"\n\
	o Usually able to master theory and abstract thinking, but don't particularly like\n\
	dealing with it unless they see a practical application\n\
	o Action-oriented \"doers\"\n\
	o Focused on living in the present, rather than the future\n\
	o Love variety and new experiences\n\
	o Highly practical and realistic\n\
	o Excellent \"trouble-shooters\", able to quickly find solutions to a wide variety of practical problems\n\
	o Results-oriented; they like to see immediate results for their efforts\n\
	o Usually laid-back and easy-going with people\n\
	o Risk-takers who thrive on action\n\
	o Independent and determined - usually dislike committing themselves\n\
	o Usually quite self-confident\n\
"
]


question_tab = [
"1.At a party do you:\n\
	1. Interact with many, including strangers\n\
	2. Interact with a few, known to you\n"
,
"2. Are you more:\n\
	1. Realistic than speculative\n\
	2. Speculative than realistic\n"
,
"3. Is it worse to:\n\
	1. Have your “head in the clouds”\n\
	2.Be “in a rut”\n"
,
"4. Are you more impressed by:\n\
	1. Principles\n\
	2. Emotions\n"
,
"5. Are more drawn toward the:\n\
	1. Convincing\n\
	2. Touching\n"
,
"6. Do you prefer to work:\n\
	1. To deadlines\n\
	2. Just “whenever”\n"
,
"7. Do you tend to choose:\n\
	1. Rather carefully\n\
	2. Somewhat impulsively\n"
,
"8. At parties do you:\n\
	1. Stay late, with increasing energy\n\
	2. Leave early with decreased energy\n"
,
"9. Are you more attracted to:\n\
	1. Sensible people\n\
	2. Imaginative people\n"
,
"10. Are you more interested in:\n\
	1. What is actual\n\
	2. What is possible\n"
,
"11. In judging others are you more swayed by:\n\
	1. Laws than circumstances\n\
	2. Circumstances than laws\n"
,
"12. In approaching others is your inclination to be somewhat:\n\
	1. Objective\n\
	2. Personal\n"
,
"13. Are you more:\n\
	1. Punctual\n\
	2. Leisurely\n"
,
"14. Does it bother you more having things:\n\
	1. Incomplete\n\
	2. Completed\n"
,
"15. In your social groups do you:\n\
	1. Keep abreast of other’s happenings\n\
	2. Get behind on the news\n"
,
"16. In doing ordinary things are you more likely to:\n\
	1. Do it the usual way\n\
	2. Do it your own way\n"
,
"17. Writers should:\n\
	1. “Say what they mean and mean what they say”\n\
	2. Express things more by use of analogy\n"
,
"18. Which appeals to you more:\n\
	1. Consistency of thought\n\
	2. Harmonious human relationships\n"
,
"19. Are you more comfortable in making:\n\
	1. Logical judgments\n\
	2. Value judgments\n"
,
"20. Do you want things:\n\
	1. Settled and decided\n\
	2. Unsettled and undecided\n"
,
"21. Would you say you are more:\n\
	1. Serious and determined\n\
	2. Easy-going\n"
,
"22. In phoning do you:\n\
	1. Rarely question that it will all be said\n\
	2. Rehearse what you’ll say\n"
,
"23. Facts:\n\
	1. “Speak for themselves”\n\
	2. Illustrate principles\n"
,
"24. Are visionaries:\n\
	1. somewhat annoying\n\
	2. rather fascinating\n"
,
"25. Are you more often:\n\
	1. a cool-headed person\n\
	2. a warm-hearted person\n"
,
"26. Is it worse to be:\n\
	1. unjust\n\
	2. merciless\n"
,
"27. Should one usually let events occur:\n\
	1. by careful selection and choice\n\
	2. randomly and by chance\n"
,
"28. Do you feel better about:\n\
	1. having purchased\n\
	2. having the option to buy\n"
,
"29. In company do you:\n\
	1. initiate conversation\n\
	2. wait to be approached\n"
,
"30. Common sense is:\n\
	1. rarely questionable\n\
	2. frequently questionable\n"
,
"31. Children often do not:\n\
	1. make themselves useful enough\n\
	2. exercise their fantasy enough\n"
,
"32. In making decisions do you feel more comfortable with:\n\
	1. standards\n\
	2. feelings\n"
,
"33. Are you more:\n\
	1. firm than gentle\n\
	2. gentle than firm\n"
,
"34. Which is more admirable:\n\
	1. the ability to organize and be methodical\n\
	2. the ability to adapt and make do\n"
,
"35. Do you put more value on:\n\
	1. infinite\n\
	2. open-minded\n"
,
"36. Does new and non-routine interaction with others:\n\
	1. stimulate and energize you\n\
	2. tax your reserves\n"
,
"37. Are you more frequently:\n\
	1. a practical sort of person\n\
	2. a fanciful sort of person\n"
,
"38. Are you more likely to:\n\
	1. see how others are useful\n\
	2. see how others see\n"
,
"39. Which is more satisfying:\n\
	1. to discuss an issue throughly\n\
	2. to arrive at agreement on an issue\n"
,
"40. Which rules you more:\n\
	1. your head\n\
	2. your heart\n"
,
"41. Are you more comfortable with work that is:\n\
	1. contracted\n\
	2. done on a casual basis\n"
,
"42. Do you tend to look for:\n\
	1. the orderly\n\
	2. whatever turns up\n"
,
"43. Do you prefer:\n\
	1. many friends with brief contact\n\
	2. a few friends with more lengthy contact\n"
,
"44. Do you go more by:\n\
	1. facts\n\
	2. principles\n"
,
"45. Are you more interested in:\n\
	1. production and distribution\n\
	2. design and research\n"
,
"46. Which is more of a compliment:\n\
	1. “There is a very logical person.”\n\
	2. “There is a very sentimental person.”\n"
,
"47. Do you value in yourself more that you are:\n\
	1. unwavering\n\
	2. devoted\n"
,
"48. Do you more often prefer the\n\
	1. final and unalterable statement\n\
	2. tentative and preliminary statement\n"
,
"49. Are you more comfortable:\n\
	1. after a decision\n\
	2. before a decision\n"
,
"50. Do you:\n\
	1. speak easily and at length with strangers\n\
	2. find little to say to strangers\n"
,

"51. Are you more likely to trust your:\n\
	1. experience\n\
	2. hunch\n"
,
"52. Do you feel:\n\
	1. more practical than ingenious\n\
	2. more ingenious than practical\n"
,
"53. Which person is more to be complimented  – one of:\n\
	1. clear reason\n\
	2. strong feeling\n"
,
"54. Are you inclined more to be:\n\
	1. fair-minded\n\
	2. sympathetic\n"
,
"55. Is it preferable mostly to:\n\
	1. make sure things are arranged\n\
	2. just let things happen\n"
,
"56. In relationships should most things be:\n\
	1. re-negotiable\n\
	2. random and circumstantial\n"
,
"57. When the phone rings do you:\n\
	1. hasten to get to it first\n\
	2. hope someone else will answer\n"
,
"58. Do you prize more in yourself:\n\
	1. a strong sense of reality\n\
	2. a vivid imagination\n"
,
"59. Are you drawn more to:\n\
	1. fundamentals\n\
	2. overtones\n"
,
"60. Which seems the greater error:\n\
	1. to be too passionate\n\
	2. to be too objective\n"
,
"61. Do you see yourself as basically:\n\
	1. hard-headed\n\
	2. soft-hearted\n"
,
"62. Which situation appeals to you more:\n\
	1. the structured and scheduled\n\
	2. the unstructured and unscheduled\n"
,
"63. Are you a person that is more:\n\
	1. routinized than whimsical\n\
	2. whimsical than routinized\n"
,
"64. Are you more inclined to be:\n\
	1. easy to approach\n\
	2. somewhat reserved\n"
,
"65. In writings do you prefer:\n\
	1. the more literal\n\
	2. the more figurative\n"
,
"66. Is it harder for you to:\n\
	1. identify with others\n\
	2. utilize others\n"
,
"67. Which do you wish more for yourself:\n\
	1. clarity of reason\n\
	2. strength of compassion\n"
,
"68. Which is the greater fault:\n\
	1. being indiscriminate\n\
	2. being critical\n"
,
"69. Do you prefer the:\n\
	1. planned event\n\
	2. unplanned event\n"
,
"70. Do you tend to be more:\n\
	1. deliberate than spontaneous\n\
	2. spontaneous than deliberate\n"
]




def clear() :
	os.system('cls||clear')

def move_next_question() :
	clear()
	global main_index
	main_index += 1

def read_answer() :
	a = 0
	while (a != '1' and a != '2') :
		a = input("to answer please press 1 or 2 then enter")
	answer_tab[main_index] = int(a)

def calculate_points():
	e = i = s = n = t = f = j = p = 0
	global answer_tab
	x = 0
	while (x < 70):
		if ((x+1)%7 == 1):
			if (answer_tab[x] == 1):
				e += 1
			elif (answer_tab[x] == 2):
				i += 1
		elif ((x+1)%7 == 2 or (x+1)%7 == 3):
			if (answer_tab[x] == 1):
				s += 1
			elif (answer_tab[x] == 2):
				n += 1
		elif ((x+1)%7 == 4 or (x+1)%7 == 5):
			if (answer_tab[x] == 1):
				t += 1
			elif (answer_tab[x] == 2):
				f += 1
		elif ((x+1)%7 == 6 or (x+1)%7 == 0):
			if (answer_tab[x] == 1):
				j += 1
			elif (answer_tab[x] == 2):
				p += 1
		x += 1
	global personality
	personality = ''
	if (e > i) :
		personality += 'E'
	else:
		personality += 'I'
	if (s > n) :
		personality += 'S'
	else:
		personality += 'N'
	if (t > f) :
		personality += 'T'
	else:
		personality += 'F'
	if (j > p) :
		personality += 'J'
	else:
		personality += 'P'

def display_personality():
	global personality_tab
	print("											 You are an " + str(personality) + "\n")

	if (personality == "ENFJ") :
		print(personality_tab[0])	
	elif (personality == "ENTJ") :
		print(personality_tab[1])
	elif (personality == "ENFP") :
		print(personality_tab[2])
	elif (personality == "ENTP") :
		print(personality_tab[3])
	elif (personality == "ESFJ") :
		print(personality_tab[4])
	elif (personality == "ESFP") :
		print(personality_tab[5])
	elif (personality == "ESTJ") :
		print(personality_tab[6])
	elif (personality == "ESTP") :
		print(personality_tab[7])
	elif (personality == "INFJ") :
		print(personality_tab[8])
	elif (personality == "INFP") :
		print(personality_tab[9])
	elif (personality == "INTJ") :
		print(personality_tab[10])
	elif (personality == "INTP") :
		print(personality_tab[11])
	elif (personality == "ISFJ") :
		print(personality_tab[12])
	elif (personality == "ISFP") :
		print(personality_tab[13])
	elif (personality == "ISTJ") :
		print(personality_tab[14])
	elif (personality == "ISTP") :
		print(personality_tab[15])





#########################################################################################

#										START

#########################################################################################
clear()
print("\
***********************************************************************************\n\
===================================================================================\n\
					Welcome\n\
In this test of 70 questions, you will learn your type of personality, good luck !\n\
===================================================================================\n\
***********************************************************************************\n\
")
while(main_index < 70) :
	print(question_tab[main_index])
	read_answer()
	move_next_question()

calculate_points()
display_personality()
print(answer_tab)



# os.system('clear')
# print(chr(27) + "[2J")

# import subprocess, platform

# if platform.system()=="Windows":
#     subprocess.Popen("cls", shell=True).communicate()
# else: #Linux and Mac
#     print("\033c", end="")

