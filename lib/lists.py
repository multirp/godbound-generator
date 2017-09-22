# Here are all of the lists that are used in the Godbound book in order to
# build a ruin or court.  These lists are laid out in what is hopefully an
# easy to see manner, and commented to tell you what list it actually is.

# This is the main purpose of the ruin
# Variable: purposeRoll
purposeList = [
    'Covert base for spies or a rebel cell',
    'Fortress or military installation',
    'Gatehouse for a Night Road',
    'Magical or high-tech transport nexus',
    'Military base or training area',
    'Mine or resource extraction site',
    'Palace for a great official',
    'Part of a ruined city or town residential area',
    'Prison camp for enemies',
    'Prison for supernatural entity',
    'Refuge for survivors of the Shattering',
    'Resort for the elite or the wealthy',
    'Sealed site of a magical disaster',
    'Semi-magical manufactory',
    'Survival bunker for government elite',
    'Temple or monastary to worship a Made God',
    'Theotechnical research site',
    'Trading nexus witih transit and storage',
    'University or arcane school',
    'Vault or treasury for some mighty relic'
    ]

# This is the main hazard roll for the ruin
# Variable: hazardRoll
hazardList = [
    'Abundant traps',
    'Autonomous defenses',
    'Crumbling structure',
    'Cyclical destruction',
    'False exterior',
    'Heritor inhabitants',
    'Honey trap',
    'Hostile environment',
    'Lethal surroundings',
    'Lingering curse',
    'Mutated guardians',
    'Perpetual war zone',
    'Remote location',
    'Sealed entrance',
    'Swarm hive',
    'Taboo wardens',
    'Temporal lock',
    'Titanic beast',
    'Toxic miasma',
    'Verticality'
    ]

# This is the main reward list for the ruin
# Variable: rewardRoll
rewardList = [
    'Arcane lore, theurgic invocation, or lost low magic',
    'Celestial shards needed for major works of Dominion',
    'Dark secret hidden by the locals or their heirs',
    'Material wealth in coins, gems, or rare substances',
    'Needed key to some other ruin, unlocking a vault',
    'Night Road entry that can be opened and closed',
    'Powerful artifact awaiting a worthy user',
    'Revealed plot or early warning of an impending disaster',
    'Token of legitimacy for the local ruling family',
    'Transport nexus allowing fast travel elsewhere',
    'Useful ally that can be negotiated or reactivated',
    'Valuable map to a treasure or to another lost ruin'
    ]


# These are the lists for the individual locations.  They are used in a while loop in order to iterate through each and every room of the ruin.

roomPurposeList = [
    'Archive, library, scriptorium, record-keeping for the site',
    'Assembly area, plaza, audience chamber, merchant shop',
    'Command area, site controls, leaders quarters',
    'Dining hall, hydroponic garden, food processing',
    'Function area for the sites original purpose',
    'Mantinence shop, janitorial area, reprocessing zone',
    'Manufactory area, industrial workplace, artisans shop',
    'Passage between locations, storage area, or vault',
    'Recreation or artistic area, tavern, gallery, private bower',
    'Sleeping or residential quarters for the inhabitants',
    'Temple or chapel to a Made God or latter deity',
    'Training area, classroom, practice field, auditorium'
    ]

roomValuablesList = [
    'Bait, to distract from a greater prize',
    'Broken or scattered in fragments',
    'hidden under or in furnishings here',
    'Left out in the open, untouched',
    'Locked away in a visible container',
    'Mixed with detrius or trash',
    'Part of the furnishings or equipment',
    'Placed with valueless similar objects',
    'Precariously placed, risking damage',
    'Repurposed for a mundane end',
    'Ridiculously well-concealed',
    'Unobtrusive but not really hidden'
    ]

roomMoodList = [
    'Bloody, the site of awful violence',
    'Brilliant with lights or high windows',
    'Cozy, with signs of recent occupation',
    'Crackling with eenrgy, motion, or sound',
    'Crumbling, its contents falling apart',
    'Dark, lamps and windows darkened',
    'Defaced and spoilt by occupants',
    'Graveyard, full of old yellowed death',
    'Kept in unusually good condition',
    'Lonely, desolate, and unvisited',
    'Patched, half-fixed by its occupants',
    'Reeking with decay and corruption'
    ]

roomMovementProblemsList = [
    'The way is behind heavy rubble',
    'The way is concealed behind something',
    'The way is dark, and light draws peril',
    'The way is false, and leads to peril',
    'The way is heavily fortified by occupants',
    'The way is locked or barred',
    'The way is opened elsewhere in the ruin',
    'The way is prone to collapse at any time',
    'The way is trapped by the occupants',
    'The way leads through lethal terrain',
    'The way leads to an awkward vantage',
    'The way requires climbing or flight'
    ]

roomPhysicalPerilList = [
    'A closed door is trapped or load-bearing',
    'Alarming noise made if a thing is handled',
    'Crumbling floors, ceilings, or walls',
    'Dangerous flames or energy discharges',
    'Heavy object topples if touched at all',
    'Noxious or toxic pools, fungi, or flora',
    'Opening a container releases a bad thing',
    'Poisonous or explosive miasma here',
    'Sites original function gone berserk',
    'Slippery or trecherous footing',
    'Time-delayed danger trigger on entry',
    'Treasure is dangerous or a trap trigger'
    ]

roomOccupantPerilList = [
    'A hidden sentinel watches the area',
    'Their champion or leader lairs here',
    'Their mates and offspring are here',
    'There are a whole lot of them here',
    'They have a superb tactical position here',
    'They have allies posted here',
    'They rush in as a swarm on an alarm',
    'They have arranged a trap for intruders',
    'They have set guard beasts to lair here',
    'They have set up a fixed but deadly weapon',
    'They have set up an ambush in the area',
    'This is a sacred place to them'
    ]

roomMagicalPerilList = [
    'Alarm when magic is sensed here',
    'Animated objects or automaton pieces',
    'Broken artifact explodes if handled',
    'Curse on those who handle something',
    'Effort-draining field on artifact',
    'Empyrean ward, as per Treasure chapter',
    'Evironment like a hostile gift effect',
    'Low magic ward or trap in place',
    'Magical counterstrike on Gift use',
    'Magical disease from an object',
    'Subtly curse target or their possessions',
    'Transform target or possessions']


# What follows is Court-related stuff.  When possible, the type of court that it
# belongs to is prepended, so you end up with stuff like
# "aristocraticCourtMood" and "aristocraticConflicts".  Yes, it's messy, but
# with the way the courts are designed, I'm not entirely sure there is a better
# way to handle things and make them easily parsable.

courtPowerStructure = [
    'Autocratic',
    'Figurehead',
    'Shared',
    'Consensus',
    'Democratic',
    'Anarchic'
    ]

# What follows applies to the Aristocratic type of court
aristocraticCourtMood = [
    'Beauty-loving, with exquisite art and architecture',
    'Bluff and familiar, with easy access to nobility',
    'Bracing for an expected clash or change of rulers',
    'Confused, with a welter of plots and counterplots',
    'Corrupt, where everything takes cash or favors to do',
    'Decadent, obsessed with exotic pleasures',
    'Decaying, hidebound by rules no longer understood',
    'Delusional, convinced of a false situation in the world',
    'Paranoid, with everyone suspected of treachery',
    'Rigidly formal with elaborate protocols enforced',
    'Vibrant with activity and bold ambition',
    'Xenophilic, eager for foreign fashions and visitors'
    ]

aristocraticMajorActors = [
    'Court sorcerer',
    'Cunning vizier',
    'Discarded former favorite',
    'Foreign ambassador',
    'Heir to rule',
    'Honored general',
    'Noble clergyman',
    'Noble family matriarch',
    'Rulers favorite courtier',
    'Rulers spouse or lover',
    'Titular ruler',
    'Treasury keeper'
    ]

aristocraticMinorActors = [
    'Amoral sycophant',
    'Commoner petitioner',
    'Court musician',
    'Disguised spy',
    'Disposable plaything',
    'Foreign artist',
    'Gossiping servant',
    'Grizzled guardsman',
    'Hired assassin',
    'Rulers personal body-servant',
    'Scheming clerk',
    'Veteran huntsman'
    ]

aristocraticPowerSources = [
    'Has access to state treasury',
    'Has assassins and criminals at their beck and call',
    'Has ties with powers in a neighboring state',
    'Has vigorous backing from a local religion',
    'Impeccable bloodline or legitimacy',
    'Important figure is utterly smitten with them',
    'Much loved by the common people',
    'Numerous family ties with other nobles',
    'Owns vast amount of personal wealth',
    'Possesses strong magic or exotic resources',
    'Spying and blackmail have armed them well',
    'Very influential with the military'
    ]

aristocraticConflicts = [
    'A favorite is being too indulged',
    'A foolish policy is being enacted',
    'A loan may or may not be repaid',
    'A marriage is being forcibly pressured',
    'A noble title is fought over',
    'Dispute over the heir',
    'Grudge over an old treachery',
    'Land ownership is in question',
    'Ownership of vital regalia is disputed',
    'Someone resents a lack of reward',
    'Someones genealogy is challenged',
    'Someones using dark sorcery'
    ]

aristocraticConsequences = [
    'A civil struggle or civil war will break out',
    'A much worse set of replacements are waiting',
    'A neighboring court would be infuriated by it',
    'A vital project would collapse disasterously',
    'Actually, nothing particularly bad would happen',
    'Hostile outsiders would seize the opportunity',
    'Many locals would be furious at the disruption',
    'No one else with any pretense of legitimacy',
    'Only they know how to work the government',
    'Their lineage is needed to operate vital magic',
    'They represent the major elements of society',
    'They are holding back a dire threat to the society'
    ]

aristocraticDefenses = [
    'A crew of bodyguard magi',
    'A magical defensive construct',
    'A very capable sorcerer',
    'An elite corps of human warriors',
    'Buildings with dire traps',
    'Extreme seclusion of the nobility',
    'Lingering magical blessing',
    'Magical guardian beast or beasts',
    'Powerful Empyrean wards',
    'Powerful personal defensive magic',
    'Swarms of trained guardsman',
    'Vast mobs of devoted servants'
    ]

# What follows pertains to the bureaucratic courts
bureaucraticCourtMood = [
    'Admired, for its probity and efficiency at its work',
    'Aristrocratic, as a refuge for excess noble offspring',
    'Autocratic, the real power behind a puppet ruler',
    'Contemptuously, as a pack of incompetent obstacles',
    'Corrupt, willing to do anything for a little silver',
    'Dangerous, where political losers tend to die young',
    'Hidebound, in opposition to all new things of any kind',
    'Irrelevant, with the real administration lying elsewhere',
    'Novel, being new to the area or full of new methods',
    'Pious, largely an outgrowth of the local majority faith',
    'Reverenced, as cultured elite due honor and respect',
    'Self-interested, only concerned with its own power'
    ]

bureaucraticMajorActors = [
    '"Retired" kingmaker',
    'Chief justice',
    'Chief spymaster',
    'Head of tax collection',
    'Head of the police',
    'Minister of Agriculture',
    'Minister of Foreign Affairs',
    'Minister of Internal Affairs',
    'Minister of Temples',
    'Minister of Trade',
    'Minister of War',
    'Secretary of a great minister'
    ]

bureaucraticMinorActors = [
    'Ambitious young clerk',
    'An officials favorite lover',
    'Clerk who spies for a rival official',
    'Crony capitalist business owner',
    'Cynical clerk seducing their way up',
    'Desperately confused petitioner',
    'Distracted record archivist',
    'Hapless tax debtor doing "favors"',
    'Litigant seeking to bribe someone',
    'Official demoted for his sins',
    'Smuggler dodging tarrifs',
    'Wizened old clerk who knows all'
    ]

bureaucraticPowerSources = [
    'Numerous important locals own them big favors',
    'Only they actually know how to operate the bureau',
    'Their peers in the brueau all admire and like them',
    'Their police ties give them legal carte blanche for much',
    'They have access to relevant state secrets',
    'They have blackmail material on their superiors',
    'They have limited but very useful legislative power',
    'They have powerful business ties they can exploit',
    'They have the means and allies to assassinate people',
    'They have ties to powerful local criminal groups',
    'They are deeply loved by the local ruler for their skills',
    'They are very personally wealthy or from a rich family'
    ]

bureaucraticConflicts = [
    'A nobel is trying to muscle the bureau',
    'A reformer wants to kick someone out',
    'A usurper seeks someones position',
    'Someone is embezzling state funds',
    'Someone is a spy for another brueau',
    'Someone is an agent of a foreign state',
    'The bureau is too rich for its own good',
    'The bureau is critically underfunded',
    'The bureaus job just got terribly hard',
    'The bureau is missing taxes or fees due',
    'The bureau is riddled with corruption',
    'The ruler is upset with the bureau'
    ]

bureaucraticConsequences = [
    'A critical project would fail with much suffering',
    'A now-unfettered rival would seize much power',
    'A rival bureaucracy would gain their portfolio',
    'A vital government function would cease',
    'An enemy nation would take advantage of it',
    'An incompetent noble would take over, badly',
    'Complete administrative paralysis of the nation',
    'Criminal powers would fill the vacuum',
    'Government secrets would scatter with clerks',
    'It would enrage the ruler or other bureaucrats',
    'Oppressed peasants would chance a revolt',
    'Unrelated services would worsen as focus shifts'
    ]

bureaucraticDefenses = [
    'A mighty wizard in their debt',
    'Confiscated magical artifacts',
    'Contingent of well-trained police',
    'Deal with a supernatural power',
    'Decentralized offices of import',
    'Detachements of regular soldiers',
    'Guardian sorcerers for the office',
    'Heavily-armed tax enforcers',
    'Not all clerks are human',
    'Operatives from the espionage arm',
    'Sheer number of clerks',
    'Venerable fixed wards'
    ]

# What follows pertains to the business courts
businessCourtMood = [
    'They are teetering on the edge of bankruptcy',
    'It has been a long, dry season of barely handing on',
    'It is a recent golden age of sudden, dramatic expansion',
    'It is chasing itself in circles, without coherent direction',
    'It is being threatened by a rival enterprise',
    'It has amade an enemy of the local officials somehow',
    'A great opportunity is present, albeit hard to exploit',
    'It is fat and happy, going on as it always has before',
    'The local ruler has an interest in its thriving',
    'It is secretly cutting corners in its products or services',
    'It is getting by on past glories, now a dwindled remnant',
    'It is trying to branch out into a new field or location'
    ]

businessMajorActors = [
    'Biggest business rival',
    'Biggest customer',
    'Brash entrepreneur',
    'Brilliant innovator',
    'Careless owners child',
    'Chief accountant',
    'Critically-skilled employee',
    'Hard-bitten founder',
    'Heir-apparent to business',
    'Main supplier of goods',
    'Major investor',
    'Popular crew foreman'
    ]

businessMinorActors = [
    '"Protection" outfit heavy',
    'Aspiring vender to the business',
    'Bribable local inspector',
    'Devoted long-time staffer',
    'Embittered ex-employee',
    'Gold-digging lover of the owner',
    'Infuriated customer',
    'Oldest employee of the business',
    'Petty thief of stock',
    'Shade black market contact',
    'Spy for a rival business',
    'Wildly impractical dreamer'
    ]

businessPowerSources = [
    'The business owes them a great deal of money',
    'The employees love them and listen to them unfailingly',
    'The others are physical afraid of their displeasure',
    'The vendors only trust them to negotiate supply buys',
    'They can legally wreck the business if too displeased',
    'They have magic or technology critical to the business',
    'They hold a secret critical to carrying out the business',
    'They know the details of a secret crime of the business',
    'They legally hold a large amount of the businesses money',
    'They own the deed to a major business facility',
    'They are holding back the local extortionists and thieves',
    'They are particularly friendly with the local ruler'
    ]

businessConflicts = [
    'A competitor is trying to buy them out',
    'A trator is working for a competitor',
    'It is struggling under a heavy debt',
    'Major actors are divided on strategy',
    'Recent effort has gone drastically bad',
    'The employees are in an uproar',
    'The locals blame it for something dire',
    'The owner is incapacitated indefinitely',
    'The ruler "asked" for a very costly favor',
    'Their survival hinges on ongoing crime',
    'They are covering up a major crime',
    'They have lost a vital secret or tool'
    ]

businessConsequences = [
    'A fragile, valuable economic link breaks up',
    'Debt chain reaction takes out a major firm',
    'It would enrage their major customers',
    'It would infuriate influential business partners',
    'Only they can provide a critical local service',
    'The local ruler relies on it for exerting control',
    'Their competitors are much more rapacious',
    'They provide critical employment to locals',
    'They are holding a community creditor at bay',
    'They are keeping out ruffians and exploiters',
    'They are paying off outside threats or grafters',
    'They are the only supplier of a vital local necessity'
    ]

businessDefenses = [
    '"Protection" outfit legbreakers',
    'A crew of burly, loyal employees',
    'Decentralized business control',
    'Expensive lawyers',
    'Heavily fortified businessplace',
    'Hired local wizard',
    'Hired mercenaries',
    'Inherited magical defenses',
    'Personally fearsome owner',
    'Protective local citizens',
    'Purchased magical defenses',
    'Special police protection'
    ]

# What follows pertains to the Community courts 
communityCourtMood = [
    'Amoral, indifferent to harm to outsiders or strangers',
    'Corrupt, dealing with bandits and the sinister',
    'Dislocated, recently forced to move or give up land',
    'Divided, two factions furious with each other',
    'Flush, enjoying new wealth from some new source',
    'Insular, polite but reluctant to deal with strangers',
    'Martial, expecting violence from the world',
    'Oppressed, afflicted by some outside power',
    'Pious, with life revolving around the community faith',
    'Placid, the locals largely content with their lot',
    'Rigid, clinging to tradition in the face of some peril',
    'Xenophobic, mistrusting outsiders as dangerous'
    ]

communityMajorActors = [
    'Best hunter or farmer',
    'Biggest gossip',
    'Chief troublemaker',
    'Hedge magician',
    'Keeper of local relics',
    'Mayor or chieftain',
    'Most eligible unwed youth',
    'Official from outside world',
    'Rich trader or merchant',
    'Rival village or tribe chief',
    'Shaman or village priest',
    'Wealthy outsider'
    ]

communityMinorActors = [
    'Adulterous spouse of major actor',
    'Bad-luck farmer or hunter',
    'Bandit seeking refuge or loot',
    'Barfly who hears all',
    'Local innkeeper or guest-keeper',
    'Local miller or tanner',
    'Naive farm lad or lass',
    'Native prodigy at some local skill',
    'Outcast suspected of evil magic',
    'Part-time prostitute',
    'Retired outsider seeking quiet',
    'Shabby vagabond'
    ]

communityPowerSources = [
    'Important outsiders will only deal with them',
    'Only they know a skill that is vital to the community',
    'Their word is taken as final in matters of tradition',
    'They have a huge family that backs them',
    'They have a powerful magical item at their disposal',
    'They have outsider friends with few scruples',
    'They have unusual wealth for the community',
    'They know secret magic or forbidden arts',
    'They know the local terrain and its useful secrets',
    'They are related to several important familes or people',
    'They are remarkably beautiful and persuasive',
    'They are very personally formidable in a fight'
    ]

communityConflicts = [
    'A family head is mistreating their kin',
    'A family is being denied its old rights',
    'A local is profiting from a dire crime',
    'A new faith is preaching to locals',
    'Dire want threatens family survival',
    'Locals struggle to own a new discovery',
    'Outsiders seeks to buy village land',
    'Outsiders seek to control the group',
    'Someone might be using dark magic',
    'Someone wants to attack a rival group',
    'Tradition is demanding a sacrifice',
    'Vital resources are being depleted'
    ]

communityConsequences = [
    'A celestial law will loosen due to lack of rites',
    'A dark power will recuit the survivors',
    'A local noble will be angry at the loss',
    'A now-unchecked threat will grow',
    'A survivor will cut a deal with a sinister power',
    'An important trade link will collapse',
    'Kin-related villages will be furious',
    'Nearby communities will lack a vital export',
    'Revolutionaries will recruit the survivors',
    'Survivors will scatter and speak of the PCs',
    'The fury of a powerful home-town hero',
    'The survivors will turn to banditry'
    ]

communityDefenses = [
    'A guardian spirit or entity',
    'A mighty retired hero',
    'A mob of angry peasants',
    'A potent local sorcerer',
    'A relic of protection or power',
    'A resident noble and his guards',
    'A secret cult with potent magic',
    'A small garrison of outside troops',
    'Bandits who need the group',
    'Close alliances with the neighbors',
    'So poor they can easily flee',
    'Trained guardian beasts'
    ]

# What follows pertains to the criminal courts
criminalCourtMood = [
    'Banditry in the surrounding area',
    'Blackmailing and spying for the rich',
    'Extortion from local merchants',
    'Fighting rival groups for turf',
    'Hired assassination and other violence',
    'Human trafficking for labor or pleasure',
    'Import of drugs or forbidden contraband',
    'Persecuting a perceived group of enemies',
    'Pickpocking and petty theft',
    'Smuggling of goods to avoid customs taxes',
    'Theft and embezzlement from the government',
    'Vices of all expensive kinds'
    ]

criminalMajorActors = [
    'Ambitious revolutionary',
    'Begger king',
    'Brothel owner',
    'Corrupt official',
    'Expert cat burglar',
    'Family patriarch',
    'Gang leader',
    'Grasping priest',
    'Loan shark',
    'Master assassin',
    'Scheming merchant',
    'Venal priest'
    ]

criminalMinorActors = [
    'Ambitious thief',
    'Bribed guardsman',
    'Canny smuggler',
    'Cynical prostitute',
    'Disposable thug',
    'Embezzling clerk',
    'Fightened shopkeep',
    'Reluctant debtor',
    'Roving pickpocket',
    'Scrawny urchin',
    'Sharp-eyed begger',
    'Well-paid lawyer'
    ]

criminalPowerSources = [
    'Controls a dangerous gang or cabal',
    'Controls fencing or money handling',
    'Handles the corrupt local officials',
    'Has a stable of urchins and/or prostitutes',
    'Has connections with the local elites',
    'Has potent magic or a powerful relic',
    'Knows secret paths and ways to anywhere',
    'Owns a number of useful front businesses',
    'Patriarch/matriarch of extended criminal family',
    'Provides a driving ideology for the group',
    'Provides muscle or murder for the group',
    'Provides social legitimacy for the group'
    ]

criminalConflicts = [
    'A lieutenant rebels against the boss',
    'An assassin is after a major actor',
    'Control of a new drug or contraband',
    'Control of an important local official',
    'Dispute over whether to kill someone',
    'Expulsion of outsiders from their turf',
    'Possession of a new-found ntreasure',
    'Revenge for a theft or offense',
    'Someone is trying to unify local gangs',
    'Someone has turned traitor to the law',
    'Subverting a source of law and order',
    'Turf struggle over working territories'
    ]

criminalConsequences = [
    'A local group relies on them for a living',
    'The ruler uses them to contain a serious rival',
    'Their affiliates provide vital financial services',
    'Their blackmail would get out, causing chaos',
    'They act as jailers to a magical danger',
    'They actually provide vital aid to the poor',
    'They bleed off otherwise-active rebels',
    'They defend an innocent group from progroms',
    'They hold back a tyrannical force of oppression',
    'They keep monsters from infesting dark places',
    'They keep practical order on the streets',
    'They retain important magical arts'
    ]

criminalDefenses = [
    'Crew of elite assassins',
    'Elaborate poisons',
    'Extremely hard to find',
    'Frame foes for crimes',
    'Hidden in fortified area',
    'Hostages or familiar threats',
    'Innocent front group',
    'Many suborned commoners',
    'Mobs of burly street thugs',
    'Several corrupt officials',
    'Stolen magical rites',
    'Treacherous seducer'
    ]

# What follows pertains to the Temple courts
templeCourtMood = [
    'Antiquated, caring only for the things of a different time',
    'Austere, refraining from visible luxury or indulgence',
    'Careless, priests little interested in spiritual duties',
    'Confused, in the midst of some great change',
    'Distracted, the priests caring about a secular matter',
    'Laboring, hard-pressed by the needs of believers',
    'Mystical, full of somewhat incomprehensible priests',
    'Opulent, jewled and golden in wild excess',
    'Rigid, uniform and disciplined in its clergy',
    'Tense, priests constantly ready to attack each other',
    'Unworldly, reluctant to get involved with secular things',
    'Vengeful, furious against the enemies or rivals'
    ]

templeMajorActors = [
    'Aged holy figure',
    'Eager reformer',
    'High priest or priestess',
    'Keeper of the relics',
    'Leader of a faithful group',
    'Magically-gifted priest',
    'Pious noble',
    'Popular preacher',
    'Propounder of a heresy',
    'Temple gaurd chief',
    'Temple treasurer',
    'Zealous crime boss'
    ]

templeMinorActors = [
    'Devoted commoner',
    'Dusty librarian',
    'Foreign pilgrim',
    'Grubble temple serf',
    'Guilt-stricken local',
    'Household priest',
    'Instructor-priest',
    'Naive monk',
    'Relic vendor',
    'Temple guardsman',
    'Temple Spy',
    'Tithe collector'
    ]

templePowerSources = [
    'A favorite of the local nobility or elite',
    'Beloved by the poor faithful of the religion',
    'Controls a vital relic of the faith',
    'Divine spouse or beloved of an important cleric',
    'Famously effective debator or apologist',
    'Has a sacred or important bloodline',
    'Has access to great wealth personally',
    'Has some useful or potent form of magic',
    'Has taught or brought up most local clergy',
    'Holds a vital position as a life-long post',
    'Knows a wealth of secrets and confessions',
    'Owns the temple building or land'
    ]

templeConflicts = [
    'A cleric seeking a pact with evil',
    'Accepting another temples authority',
    'Change of the temples political focus',
    'Control of a powerful, naive believer',
    'Enlisting an unsavory group of allies',
    'Major cleric pursuing a secret vise',
    'Obscure but vital theological dispute',
    'Overthrow of a troublesome local',
    'Performing a dangerous magic rite',
    'Quarrel over control of the treasury',
    'Selling a mighty relic or great treasure',
    'Silencing of a problematic priest'
    ]

templeConsequences = [
    'A curse will fall upon desecrators',
    'A dangerous cult will fill the void',
    'Government needs its support for legitimacy',
    'It will infuriate a foreign branch of the faith',
    'It is maintaining vital spiritual defenses',
    'It is sealing away a terrible power',
    'Its destruction will incite a violent prophet',
    'Local believers will be riotous',
    'Only it knows how to perform a vital service',
    'The local poor rely on temple charity',
    'The local rulers will be outraged',
    'Will cause drastic celestial damage to local laws'
    ]

templeDefenses = [
    'Powerful priestly magic',
    'Animated idol',
    'Divine blessings on temple',
    'Divine curse on assailants',
    'Many sturdy guardsmen',
    'Infuriated mob',
    'Noble patrons',
    'Sacred beast or summons',
    'Fortified temple',
    'Fanatical zealots',
    'Powerful defensive relics',
    'Wards against divine powers'
    ]