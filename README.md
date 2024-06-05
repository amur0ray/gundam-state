# gundam-state
Testing the python library `pytransitions`
https://github.com/pytransitions/transitions

Modeling the transitions between the different modes a Gundam can take.
Still learning the resource, so plans are loose. Should define at least 2
common actions: move and attack.

## Gundam, Gunship, Airframe
Could build a base for other features around a simple Pokemon-style form
countering game, but with the ability to transform modes to succeed.

Gundams can be in one of three modes:
- Fighter (Gundam)
- Airframe
- Docked (Gunship)

Mode Counters will be:
- Gundam counters Airframe (melee, fast and close range)
- Airframe counters Gunship (ranged, fastest and medium range)
- Gunship counters Gundam (magic, slow and long range)

### Gundam VS Gundam
- can equip gun to get early attack damage before melee range is closed
- DRAW

### Gundam VS Airframe
- having greater freedom of movement makes it difficult for Airframe to attack
Gundams
- can equip gun and get edge with advanced tracking
- Gundam DOMINATES

### Gundam VS Gunship
- cannot compete at range
- boarding the Gunship will assassinate the Gunship
- has great difficulty dodging AOE shells
- Gunship DOMINATES

### Airframe VS Airframe
- dogfights come down to maneuverability
- victory to whoever can get behind the other
- DRAW

### Airframe VS Gunship
- Airframe is faster than the shells of the Gunship
- Airframe can close the gap and land continuous strikes
- Gunship's only chance is to corner the Airframe and shoot in its predicted path
- Airframe DOMINATES

### Gunship VS Gunship
- must strike first, so predicting where to send shells is most important
- DRAW

## Battle Board
Could implement a simple board game, with tile distances and attack ranges per
Gundam.

### Submodes:
- Gundam has Sword and Rifle
- Airframe has Main Gun and Bombs
- Gunship has Long Range and AOE Rounds