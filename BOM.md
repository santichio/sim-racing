# Bill of Materials

Compiled parts lists for every subsystem in this repo. This is a compilation of
**other people's open-source projects** — see [Credits](./README.md#credits) for
who designed what.

> [!IMPORTANT]
> **This file is generated.** The CSVs in [`src/bom/`](./src/bom) are the source of
> truth — edit those, then run `python3 tools/build-bom.py`.

**Conventions**

- **No purchase links.** The upstream sources were full of Amazon/AliExpress
  affiliate shortlinks that rot quickly and cannot be verified. Manufacturer and
  standard part numbers (`DIN7991`, `6800-ZZ`, `JKK60-5-C-150-A1-F4-M`) are kept —
  those are the durable sourcing information.
- **Blank quantity** means the upstream source genuinely did not state one. Nothing
  here is guessed.
- **`TODO:`** marks a part the source references but never specifies.
  **`VERIFY:`** marks a contradiction in the source. Both are listed in
  [Known gaps](#known-gaps).
- **`ALTERNATIVE n of m`** means pick one — those quantities are *not* additive.

## Contents

- [Wheelbase](#wheelbase) — 12 line items
- [Pedals](#pedals) — 39 line items
- [Steering Wheel Rim](#wheel-rim) — 10 line items
- [Shifter](#shifter) — 45 line items
- [Handbrake](#handbrake) — 11 line items
- [Rig Chassis](#chassis) — 7 line items
- [Consolidated hardware list](#consolidated-hardware-list)
- [Known gaps](#known-gaps)

<a id="wheelbase"></a>

## Wheelbase

### Electronics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| OpenFFBoard controller | — | STM32-based | 1 | Control enclosure | Open-hardware FFB controller; handles the force feedback physics over USB. TODO: board revision and qty not specified in source |
| Motor driver | ODrive | — | — | Control enclosure | ALTERNATIVE 1 of 3 - pick one driver. TODO: model/qty not specified in source |
| Motor driver | VESC | — | — | Control enclosure | ALTERNATIVE 2 of 3 - pick one driver. TODO: model/qty not specified in source |
| AC servo driver | AASD-15A | — | — | Control enclosure | ALTERNATIVE 3 of 3 - pick one driver. Controlled from the OpenFFBoard via SPI/PWM. TODO: qty not specified in source |
| AC servo motor | 130ST-M10010 | Mige 130ST series; approx. 10-15 Nm | — | Wheelbase mount | ALTERNATIVE 1 of 2 - pick one motor for the target torque. TODO: qty not specified in source |
| AC servo motor | 130ST-M15015 | Mige 130ST series; approx. 20-30 Nm | — | Wheelbase mount | ALTERNATIVE 2 of 2 - pick one motor for the target torque. TODO: qty not specified in source |
| Emergency stop switch | — | — | — | E-Stop housing | TODO: implied by the printed E-Stop housing but the switch itself is not specified in source |
| Encoder | — | — | — | Motor shaft | TODO: implied by the printed encoder mounting bracket but the encoder itself is not specified in source |

### 3D printed parts

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Cable management enclosure | — | — | — | Wheelbase | TODO: qty/material not specified in source |
| Quick-release locking ring | — | — | — | Wheel side of shaft | TODO: qty/material not specified in source |
| E-Stop housing | — | — | — | Rig | TODO: qty/material not specified in source |
| Encoder mounting bracket | — | — | — | Motor rear | TODO: qty/material not specified in source |

<a id="pedals"></a>

## Pedals

### Electronics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Integrated servo motor | iSV57T-130S | — | 1 | Rail | VERIFY: named in the source section heading and in the rail kit note but never given its own line item in the upstream part tables |
| Controller PCB | — | — | 1 | PCB spacer mount | VERIFY: an 'Attach PCB' assembly step exists upstream but the PCB itself is not listed as a part; see the DIY-Sim-Racing-FFB-Pedal electronics BOM |
| Load cell | — | — | 1 | Loadcell arm | VERIFY: referenced throughout the upstream guide (loadcell arm / upper loadcell joint) but never listed as a part |

### Mechanics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Linear rail with ball screw | JKK60-5-C-150-A1-F4-M | KK60 series | 1 | Base | Available as a servo + rail + coupler kit |
| Shaft coupler 8mm to 8mm | — | 8mm-8mm | 1 | Servo to ball screw | Target spacing between motor flange and coupler is approx. 5.5 mm |
| Aluminium extrusion | — | 3060 x 400mm | 1 | Base plate | Allows direct screw-on of the linear rail and flexible rig mounting |

### Bearings

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Deep groove ball bearing | 608-ZZ | 8x22x7 (ID/OD/W) | 2 | Loadcell arm | — |
| Screw bearing | JS695-13-5C3L8M6 | — | 2 | Pedal arm to 3060 extrusion | — |

### 3D printed parts

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Loadcell arm (back) | — | — | 1 | Loadcell arm | Print in PETG-CF; 10 perimeters, 10 top/bottom, 20% infill, 270C hotend, 70C bed |
| Loadcell arm (front) | — | — | 1 | Loadcell arm | Print in PETG-CF; 10 perimeters, 10 top/bottom, 20% infill, 270C hotend, 70C bed |
| 3060 adapter plate | — | — | 1 | Rail to 3060 profile | Print in PETG-CF |
| Pedal arm | — | — | 1 | Pedal arm | Print in PETG-CF; extra width reduces flex under off-centre load |
| Faceplate | — | — | 1 | Pedal arm | Print in PETG-CF |
| Side guard | — | — | 2 | Faceplate | Print in PETG-CF |
| Upper loadcell arm adapter | — | 8mm | 2 | Loadcell to pedal arm | Print in 83A-TPE; 4 perimeters, 0 top/bottom, 90% infill, 250C hotend, 70C bed. Absorbs system noise and vibration |
| Lower loadcell arm adapter | — | 8mm | 2 | Loadcell arm to sled | Print in 83A-TPE; 4 perimeters, 0 top/bottom, 90% infill, 250C hotend, 70C bed. Absorbs system noise and vibration |
| Rail side cover (left) | — | — | 1 | Rail | Print in PETG-CF |
| Rail side cover (right) | — | — | 1 | Rail | Print in PETG-CF |
| 3060 end cover | — | — | 2 | 3060 extrusion ends | Print in PETG-CF |
| PCB spacer | — | — | 2 | PCB | Print in PETG-CF |

### Fasteners

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Cylinder head screw | — | M8x16 | 2 | Loadcell arm | — |
| Threaded rod | — | M8x45 | 2 | Loadcell arm | — |
| Cylinder head screw | — | M4x16 | 4 | Servo to rail | — |
| Cylinder head screw | — | M5x20 | 4 | Rail to 3060 profile | — |
| Cylinder head screw | — | M5x20 | 6 | Side guards | — |
| Cylinder head screw | — | M5x20 | 2 | PCB | VERIFY: upstream table labels this M5x20 but links an M5x40 product |
| Cylinder head screw | — | M5x30 | 2 | Faceplate to pedal arm | — |
| Cylinder head screw | — | M5x40 | 4 | Loadcell to pedal arm | — |
| Cylinder head screw | — | M5x25 | 4 | Loadcell arm to sled | — |
| Countersunk screw | — | M2.5x6 | 4 | Rail side covers | — |
| Wood/self-tapping screw | — | 3.5x30 | 6 | Pedal arm | Driven across print layers to increase layer bonding |
| Wood/self-tapping screw | — | 3.5x20 | 2 | Pedal arm | Driven across print layers to increase layer bonding |
| Spring ball T-nut | — | 3030 M5 | 4 | 3060 extrusion | — |
| Spring ball T-nut | — | 3030 M6 | 2 | 3060 extrusion | — |
| Flat washer | — | M6 12x1.6 | 2 | Pedal arm to 3060 extrusion | — |

### Consumables

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| PETG-CF filament | — | — | — | — | Carbon-fibre filled PETG for all rigid printed parts |
| TPE filament | — | 83A shore | — | — | For the upper and lower loadcell arm adapters |
| PTFE (Teflon) tape | — | — | 1 | Loadcell arm | Reduces play between the threaded rod and the bearing |

### Tools

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Countersink set | — | — | 1 | — | Used to remove material for the countersunk screws in the pedal arm |

<a id="wheel-rim"></a>

## Steering Wheel Rim

### Electronics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Microcontroller | Arduino Pro Micro | — | — | Wheel plate | ALTERNATIVE 1 of 2 - pick one MCU. Runs SimHub firmware. TODO: qty not specified in source |
| Microcontroller | Teensy | — | — | Wheel plate | ALTERNATIVE 2 of 2 - pick one MCU. Runs SimHub firmware. TODO: model/qty not specified in source |
| Telemetry display | VoCore | 4.3 inch | — | Wheel plate centre | ALTERNATIVE 1 of 2 - pick one display. Shows RPM, gear, lap deltas, tyre temps. TODO: qty not specified in source |
| Telemetry display | Nextion | — | — | Wheel plate centre | ALTERNATIVE 2 of 2 - pick one display. TODO: model/size/qty not specified in source |
| Addressable RGB LED | WS2812B | — | — | Shift light strip | TODO: LED count not specified in source |
| Rotary encoder | — | — | — | Wheel plate | TODO: qty not specified in source |
| Tactile microswitch | — | — | — | Magnetic paddle shifters | TODO: qty not specified in source (typically 2 - one per paddle) |

### Mechanics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Neodymium magnet | — | — | — | Magnetic paddle shifters | Provides the paddle detent feel. TODO: size/qty not specified in source |

### 3D printed parts

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Wheel plate | — | — | — | Wheel | Print reinforced in PETG, ABS, or carbon-fibre composite filament. CAD from OpenSimRacer or community files on Thingiverse/Printables (F1 or GT3 style). TODO: qty/material choice not specified in source |
| Paddle shifter | — | — | — | Behind wheel plate | Uses neodymium magnets plus tactile microswitches. TODO: qty not specified in source (typically 2) |

<a id="shifter"></a>

## Shifter

### Electronics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Custom PCB | — | — | 1 | Body 2 | Included in the Industry&CNC mechanical kit; replacements can be ordered separately |
| Arduino Micro | ATmega32U4 | — | 1 | Mounts to custom PCB | Included in the mechanical kit |
| Hall effect sensor | A3144 | — | — | Body 2 | VERIFY: referenced upstream only via the heat-shrink item ('mainly for the A3144 hall sensors') but never listed as a part with a quantity |
| Push button | — | — | 3 | Button plate mod (BP) | The upstream design is optimised for one specific button model |
| Switch | — | — | 3 | Button plate mod (BP) | The upstream design is optimised for one specific switch model |
| Switch SPDT 1A | — | — | 1 | Base lever | Included in the mechanical kit |
| Limit switch | KW11 | — | 1 | Sequential holder | Included in the mechanical kit |
| Dupont and JST connector kit | — | — | 1 | PCB | Order the matching crimp tool as well for a clean job |
| Hook-up wire 24AWG | — | — | 1 | Yellow for sequential, white for reverse, red for 5V, black for ground | At least red and black plus one more colour |
| Heat shrink tubing | — | — | 1 | Hall sensor pins | Mainly for insulating the A3144 hall sensor pins |

### Mechanics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Lever | — | Custom 12mm axle with M10x1.5 end | 1 | Lever base | Part of the Industry&CNC kit. Each part is machined to match the custom design, so processing time can take up to 7 days |
| Main axle | — | 10mm custom axle | 1 | Crank | Part of the Industry&CNC kit. Shafts can be 1-2mm longer than stated; this is normal |
| Shaft 12mm | — | 12x116mm | 1 | Low shaft | Part of the Industry&CNC kit |
| Shaft 12mm | — | 12x85mm | 1 | Rear shaft | Part of the Industry&CNC kit |
| Shaft 4mm | — | 4x100mm | 2 | Body 2 | Part of the Industry&CNC kit |
| Shaft support block | SHF12 | 12mm bore | 4 | Crank and lever | — |
| Shaft support block | SHF10 | 10mm bore | 1 | Crank | — |
| Hex nut | — | M10 | 1 | Main axle | — |
| O-ring | — | ID 11mm / 2mm section | 2 | Rear shaft and turn | — |
| Round magnet | — | 8x4mm | 1 | Turn | Part of the Industry&CNC kit |

### Bearings

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Radial spherical plain bearing | GEG12C | — | 1 | Body 1 | — |
| Deep groove ball bearing | 6800-ZZ | 10x19x5 (ID/OD/W) | 3 | Slider and main axle | — |
| Deep groove ball bearing | 698-ZZ | 8x19x6 (ID/OD/W) | 1 | Carriage | — |
| Deep groove ball bearing | 695-ZZ | 5x13x4 (ID/OD/W) | 9 | No-turn (6), turn (1), body 2 (2) | — |

### Fasteners

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Flat-head countersunk screw | DIN7991 | M4x12 | 6 | Radial joint lock (4), rear bearing holder (2) | — |
| Flat-head countersunk screw | DIN7991 | M4x30 | 2 | Servo mount | — |
| Flat-head countersunk screw | DIN7991 | M5x20 | 3 | No-turn | — |
| Flat-head countersunk screw | DIN7991 | M5x25 | 4 | Body 2 | — |
| Cylinder head screw | DIN912 | M2x10 | 5 | Switches (4), sequential holder (1) | — |
| Cylinder head screw | DIN912 | M4x40 | 2 | Reverse lock and carriage | — |
| Cylinder head screw | DIN912 | M8x10 | 1 | Body 1 | — |
| Button head screw | ISO7380 | M3x8 | 5 | PCB and PCB cover | — |
| Button head screw | ISO7380 | M5x16 | 4 | Body 2 (2), no-turn (2) | — |
| Button head screw | ISO7380 | M5x20 | 2 | Rear crank | — |
| Button head screw | ISO7380 | M5x30 | 6 | Crank | — |
| Button head screw | ISO7380 | M5x55 | 1 | Turn | — |
| Limit screw | — | M4x25 (D5) | 2 | Base lever | — |
| Grub screw | — | M5x20 | 1 | Preload | — |

### Springs

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Compression spring | — | OD 8mm, ID 4mm, L 15mm, yellow | 2 | Carriage | Included in the mechanical kit |
| Compression spring | — | OD 8mm, ID 4mm, L 35mm, yellow | 1 | Base lever | Included in the mechanical kit |
| Compression spring | — | OD 30mm, ID 15mm, L 25mm, yellow | 1 | Main axle | Included in the mechanical kit |

### Consumables

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| PLA filament | — | 1.3 kg | — | — | Total print weight for the whole gearbox |
| Gear knob | — | M10x1.5 thread | 1 | Lever | M10x1.5 gear knobs fit directly; any other knob needs an adapter |

### Tools

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Soldering iron | — | — | 1 | — | — |
| Solder wire | — | 1mm | 1 | — | — |

<a id="handbrake"></a>

## Handbrake

### Electronics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Hydraulic pressure sensor | — | 500 psi / 1/8in NPT | 1 | Banjo on brake caliper | Outputs 0.4-4.5V. Consider a 1000 psi sensor only if you push extremely hard; the upstream author never exceeded 60% of the 500 psi range |
| Cable 3-core 22AWG | — | 4mm outer diameter | 1 | Sensor to controller | Sold by length; upstream does not specify a run length |

### Mechanics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Handbrake lever assembly | — | — | 1 | Lever | — |
| Brake caliper | — | Single piston (type A) | 1 | Lever base | — |
| Master cylinder | — | — | — | Lever | TODO: required by the 3/8-24 UNF banjo item but never specified in the upstream parts list; size and bore not stated |
| Banjo bolt with pressure sensor mount | — | M10x1.25 | 1 | Between brake caliper and pressure sensor | — |
| Banjo bolt | — | 3/8-24 UNF | 1 | Master cylinder | — |
| Brake hose | — | — | 1 | Caliper to master cylinder | — |
| Banjo washers / seals | — | — | — | Both banjo bolts | Upstream lists these only as 'joints' with no size or quantity. TODO: confirm count (typically 2 per banjo bolt) |

### Fasteners

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Flat-head countersunk screw | DIN7991 | M5x35 | 3 | Frame | — |
| Cylinder head screw | DIN912 | M8x40 | 2 | Frame | — |

<a id="chassis"></a>

## Rig Chassis

### Mechanics

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Aluminium extrusion | — | 8020 4080 profile | — | Frame | Do NOT 3D print structural chassis parts - they flex under direct drive and load cell braking loads. TODO: lengths/qty not specified in source; OpenSimRacing publishes free cutting plans |
| Aluminium extrusion | — | 8020 40160 profile | — | Frame | Heavier profile for the main rails. TODO: lengths/qty not specified in source; OpenSimRacing publishes free cutting plans |

### 3D printed parts

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Cable clip | — | — | — | Frame | TODO: qty/material not specified in source |
| Button box mount | — | — | — | Frame | TODO: qty/material not specified in source |
| Mouse/keyboard tray hinge | — | — | — | Tray | TODO: qty/material not specified in source |
| Transducer / bass shaker mount | — | — | — | Seat and pedal deck | TODO: qty/material not specified in source |

### Fasteners

| Item | Part no. | Spec | Qty | Location | Notes |
|---|---|---|---|---|---|
| Extrusion brackets / T-nuts / bolts | — | — | — | Frame joints | TODO: not enumerated in source - see the OpenSimRacing hardware bill of materials for the chosen layout |

<a id="consolidated-hardware-list"></a>

## Consolidated hardware list

Fasteners, bearings and springs summed across **every** subsystem and every
assembly step, so repeated parts are ordered once. Grouped on item + part number +
spec, so a countersunk `DIN7991 M5x20` is never merged with a button-head
`ISO7380 M5x20`.

### Fasteners

| Item | Part no. | Spec | Total qty | Used in |
|---|---|---|---|---|
| Extrusion brackets / T-nuts / bolts | — | — | **—** | Rig Chassis (1) |
| Wood/self-tapping screw | — | 3.5x20 | **2** | Pedals (1) |
| Wood/self-tapping screw | — | 3.5x30 | **6** | Pedals (1) |
| Spring ball T-nut | — | 3030 M5 | **4** | Pedals (1) |
| Spring ball T-nut | — | 3030 M6 | **2** | Pedals (1) |
| Countersunk screw | — | M2.5x6 | **4** | Pedals (1) |
| Cylinder head screw | — | M4x16 | **4** | Pedals (1) |
| Limit screw | — | M4x25 (D5) | **2** | Shifter (1) |
| Cylinder head screw | — | M5x20 | **12** | Pedals (3) |
| Grub screw | — | M5x20 | **1** | Shifter (1) |
| Cylinder head screw | — | M5x25 | **4** | Pedals (1) |
| Cylinder head screw | — | M5x30 | **2** | Pedals (1) |
| Cylinder head screw | — | M5x40 | **4** | Pedals (1) |
| Flat washer | — | M6 12x1.6 | **2** | Pedals (1) |
| Cylinder head screw | — | M8x16 | **2** | Pedals (1) |
| Threaded rod | — | M8x45 | **2** | Pedals (1) |
| Flat-head countersunk screw | DIN7991 | M4x12 | **6** | Shifter (1) |
| Flat-head countersunk screw | DIN7991 | M4x30 | **2** | Shifter (1) |
| Flat-head countersunk screw | DIN7991 | M5x20 | **3** | Shifter (1) |
| Flat-head countersunk screw | DIN7991 | M5x25 | **4** | Shifter (1) |
| Flat-head countersunk screw | DIN7991 | M5x35 | **3** | Handbrake (1) |
| Cylinder head screw | DIN912 | M2x10 | **5** | Shifter (1) |
| Cylinder head screw | DIN912 | M4x40 | **2** | Shifter (1) |
| Cylinder head screw | DIN912 | M8x10 | **1** | Shifter (1) |
| Cylinder head screw | DIN912 | M8x40 | **2** | Handbrake (1) |
| Button head screw | ISO7380 | M3x8 | **5** | Shifter (1) |
| Button head screw | ISO7380 | M5x16 | **4** | Shifter (1) |
| Button head screw | ISO7380 | M5x20 | **2** | Shifter (1) |
| Button head screw | ISO7380 | M5x30 | **6** | Shifter (1) |
| Button head screw | ISO7380 | M5x55 | **1** | Shifter (1) |

### Bearings

| Item | Part no. | Spec | Total qty | Used in |
|---|---|---|---|---|
| Deep groove ball bearing | 608-ZZ | 8x22x7 (ID/OD/W) | **2** | Pedals (1) |
| Deep groove ball bearing | 6800-ZZ | 10x19x5 (ID/OD/W) | **3** | Shifter (1) |
| Deep groove ball bearing | 695-ZZ | 5x13x4 (ID/OD/W) | **9** | Shifter (1) |
| Deep groove ball bearing | 698-ZZ | 8x19x6 (ID/OD/W) | **1** | Shifter (1) |
| Radial spherical plain bearing | GEG12C | — | **1** | Shifter (1) |
| Screw bearing | JS695-13-5C3L8M6 | — | **2** | Pedals (1) |

### Springs

| Item | Part no. | Spec | Total qty | Used in |
|---|---|---|---|---|
| Compression spring | — | OD 30mm, ID 15mm, L 25mm, yellow | **1** | Shifter (1) |
| Compression spring | — | OD 8mm, ID 4mm, L 15mm, yellow | **2** | Shifter (1) |
| Compression spring | — | OD 8mm, ID 4mm, L 35mm, yellow | **1** | Shifter (1) |

`+?` means at least one contributing line item had no stated quantity.

<a id="known-gaps"></a>

## Known gaps

36 line items carry a `TODO:` or `VERIFY:` flag. These are faults in the upstream
sources that were preserved rather than papered over — resolve them before ordering.

| Subsystem | Item | Flag |
|---|---|---|
| Wheelbase | OpenFFBoard controller | **TODO** — board revision and qty not specified in source |
| Wheelbase | Motor driver | **TODO** — model/qty not specified in source |
| Wheelbase | Motor driver | **TODO** — model/qty not specified in source |
| Wheelbase | AC servo driver | **TODO** — qty not specified in source |
| Wheelbase | AC servo motor | **TODO** — qty not specified in source |
| Wheelbase | AC servo motor | **TODO** — qty not specified in source |
| Wheelbase | Emergency stop switch | **TODO** — implied by the printed E-Stop housing but the switch itself is not specified in source |
| Wheelbase | Encoder | **TODO** — implied by the printed encoder mounting bracket but the encoder itself is not specified in source |
| Wheelbase | Cable management enclosure | **TODO** — qty/material not specified in source |
| Wheelbase | Quick-release locking ring | **TODO** — qty/material not specified in source |
| Wheelbase | E-Stop housing | **TODO** — qty/material not specified in source |
| Wheelbase | Encoder mounting bracket | **TODO** — qty/material not specified in source |
| Pedals | Integrated servo motor | **VERIFY** — named in the source section heading and in the rail kit note but never given its own line item in the upstream part tables |
| Pedals | Controller PCB | **VERIFY** — an 'Attach PCB' assembly step exists upstream but the PCB itself is not listed as a part; see the DIY-Sim-Racing-FFB-Pedal electronics BOM |
| Pedals | Load cell | **VERIFY** — referenced throughout the upstream guide (loadcell arm / upper loadcell joint) but never listed as a part |
| Pedals | Cylinder head screw | **VERIFY** — upstream table labels this M5x20 but links an M5x40 product |
| Steering Wheel Rim | Microcontroller | **TODO** — qty not specified in source |
| Steering Wheel Rim | Microcontroller | **TODO** — model/qty not specified in source |
| Steering Wheel Rim | Telemetry display | **TODO** — qty not specified in source |
| Steering Wheel Rim | Telemetry display | **TODO** — model/size/qty not specified in source |
| Steering Wheel Rim | Addressable RGB LED | **TODO** — LED count not specified in source |
| Steering Wheel Rim | Rotary encoder | **TODO** — qty not specified in source |
| Steering Wheel Rim | Tactile microswitch | **TODO** — qty not specified in source (typically 2 - one per paddle) |
| Steering Wheel Rim | Neodymium magnet | **TODO** — size/qty not specified in source |
| Steering Wheel Rim | Wheel plate | **TODO** — qty/material choice not specified in source |
| Steering Wheel Rim | Paddle shifter | **TODO** — qty not specified in source (typically 2) |
| Shifter | Hall effect sensor | **VERIFY** — referenced upstream only via the heat-shrink item ('mainly for the A3144 hall sensors') but never listed as a part with a quantity |
| Handbrake | Master cylinder | **TODO** — required by the 3/8-24 UNF banjo item but never specified in the upstream parts list; size and bore not stated |
| Handbrake | Banjo washers / seals | **TODO** — confirm count (typically 2 per banjo bolt) |
| Rig Chassis | Aluminium extrusion | **TODO** — lengths/qty not specified in source; OpenSimRacing publishes free cutting plans |
| Rig Chassis | Aluminium extrusion | **TODO** — lengths/qty not specified in source; OpenSimRacing publishes free cutting plans |
| Rig Chassis | Extrusion brackets / T-nuts / bolts | **TODO** — not enumerated in source - see the OpenSimRacing hardware bill of materials for the chosen layout |
| Rig Chassis | Cable clip | **TODO** — qty/material not specified in source |
| Rig Chassis | Button box mount | **TODO** — qty/material not specified in source |
| Rig Chassis | Mouse/keyboard tray hinge | **TODO** — qty/material not specified in source |
| Rig Chassis | Transducer / bass shaker mount | **TODO** — qty/material not specified in source |

