# CS 394R Final Project: Deep Kart Racing

## Installation
NOTE: This requires that the host machine has `conda` installed.

Give it a minute or 10.
```
source install.sh
```

## Usage

The current configuration is for 8+ core machine with GPU (GTX 1080ti or better).  
Check `spc/train.py` for more details, but this is a minimal example of a policy trained with PPO that trains within an hour.

```
python3 -m spc.train --algorithm ppo \
  --gamma 0.9 \
  --lr 5e-4 \
  --batch_size 256 \
  --frame_skip 1 \
  --iterations 10 \
  --max_frames 10000
```

 * 'abyss'
 * 'arena_candela_city'
 * 'battleisland'
 * 'black_forest'
 * 'candela_city'
 * 'cave'
 * 'cocoa_temple'
 * 'cornfield_crossing'
 * 'endcutscene'
 * 'featunlocked'
 * 'fortmagma'
 * 'gplose'
 * 'gpwin'
 * 'gran_paradiso_island'
 * 'hacienda'
 * 'icy_soccer_field'
 * 'introcutscene'
 * 'introcutscene2'
 * 'lasdunasarena'
 * 'lasdunassoccer'
 * 'lighthouse'
 * 'mines'
 * 'minigolf'
 * 'olivermath'
 * 'overworld'
 * 'ravenbridge_mansion'
 * 'sandtrack'
 * 'scotland'
 * 'snowmountain'
 * 'snowtuxpeak'
 * 'soccer_field'
 * 'stadium'
 * 'stk_enterprise'
 * 'temple'
 * 'tutorial'
 * 'volcano_island'
 * 'xr591'
 * 'zengarden'

