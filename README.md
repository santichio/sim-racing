# sim-racing

A curated index of **open-source DIY sim racing hardware** — wheelbase, pedals, wheel
rim, shifter, handbrake and rig chassis — with the parts lists compiled into one
consistent, machine-readable [bill of materials](./BOM.md).

None of this hardware is original work. This repo collects designs published by the
OpenFFBoard, DIY-Sim-Racing-FFB-Pedal, Lebois Racing and OpenSimRacing projects, records
what each build actually needs, and points back at the people who designed it. See
[Credits](#credits).

> [!WARNING]
> **A direct drive wheelbase is genuinely dangerous.** A 20–30 Nm motor can sprain or
> break a wrist, and will happily throw a wheel rim across a room. Never power a DD
> wheelbase without a working emergency stop, never bolt one to a desk, and configure a
> conservative torque limit before your first spin. Treat hydraulic handbrake and brake
> lines as pressure equipment. **Build at your own risk.**

## Contents

- [Bill of Materials](#bill-of-materials)
- [Cost estimate](#cost-estimate)
- [Wheelbase](#wheelbase)
- [Pedals](#pedals)
- [Steering Wheel Rim](#steering-wheel-rim)
- [Shifter](#shifter)
- [Handbrake](#handbrake)
- [Rig Chassis](#rig-chassis)
- [Repository structure](#repository-structure)
- [Credits](#credits)
- [License](#license)

## Bill of Materials

Every subsystem has a parts list under [`src/bom/`](./src/bom) using one shared CSV
schema, aggregated into a single generated [**BOM.md**](./BOM.md).

| Subsystem | Approach | Parts | BOM | Completeness |
|---|---|---:|---|---|
| [Wheelbase](#wheelbase) | OpenFFBoard + AC servo, direct drive | 12 | [csv](./src/bom/bom-wheelbase.csv) · [md](./BOM.md#wheelbase) | Skeleton — derived from the notes below |
| [Pedals](#pedals) | Active FFB pedal, mostly 3D printed | 39 | [csv](./src/bom/bom-pedals.csv) · [md](./BOM.md#pedals) | Complete — from the upstream build guide |
| [Steering Wheel Rim](#steering-wheel-rim) | 3D printed GT3 plate + SimHub electronics | 10 | [csv](./src/bom/bom-wheel-rim.csv) · [md](./BOM.md#wheel-rim) | Skeleton — derived from the notes below |
| [Shifter](#shifter) | Lebois SRT gearbox, H-pattern + sequential | 45 | [csv](./src/bom/bom-shifter.csv) · [md](./BOM.md#shifter) | Complete — from the upstream kit list |
| [Handbrake](#handbrake) | Hydraulic, pressure-sensor based | 11 | [csv](./src/bom/bom-handbrake.csv) · [md](./BOM.md#handbrake) | Complete — from the upstream parts list |
| [Rig Chassis](#rig-chassis) | 8020 aluminium extrusion | 7 | [csv](./src/bom/bom-chassis.csv) · [md](./BOM.md#chassis) | Skeleton — derived from the notes below |

Conventions worth knowing before you order anything:

- **No purchase links.** The upstream lists were full of affiliate shortlinks that rot
  fast. Manufacturer and standard part numbers are kept instead — those are durable.
- **A blank quantity means the source never stated one.** Nothing is guessed.
- **[Known gaps](./BOM.md#known-gaps)** lists every part flagged `TODO` (referenced but
  never specified) or `VERIFY` (the source contradicts itself). Read it first.

The CSVs are the source of truth. After editing one, regenerate the aggregate:

```sh
python3 tools/build-bom.py          # rewrite BOM.md
python3 tools/build-bom.py --check  # fail if BOM.md is stale
```

## Cost estimate

The BOM carries **no prices** — see the convention above. A separate, hand-made market
estimate lives in [`docs/cost-estimate.md`](./docs/cost-estimate.md): roughly **€2,350**
for a lean build (10 Nm motor, two active pedals, sourced direct from China), **€3,600**
mid, **€4,900** for EU-sourced parts and a larger frame — before VAT, duty, a seat, or a
printer that can handle PETG-CF.

Those numbers are an estimate, not a quote, and they are deliberately kept out of the
CSVs so the parts lists stay verifiable against their upstream sources.

## Wheelbase

<!-- Photo of the assembled OpenFFBoard wheelbase goes here (assets/wheelbase.jpeg). -->

OpenFFBoard + servo motor. Direct drive (DD), 10–30 Nm of torque.

- **Core controller:** OpenFFBoard (Open Force Feedback Board). An open-hardware,
  STM32-based controller dedicated to FFB physics calculations over USB.
- **Motor driver:** ODrive, VESC, or a dedicated AC servo driver (e.g. AASD-15A
  controlled via SPI/PWM).
- **Motor:** industrial AC servo motor like the Mige 130ST series — 130ST-M10010 for
  ~10–15 Nm, or 130ST-M15015 for ~20–30 Nm.
- **3D printed roles:** cable management enclosures, quick-release locking rings,
  emergency stop (E-Stop) housings, and encoder mounting brackets.

📋 **[Wheelbase BOM](./BOM.md#wheelbase)**

### References

- [OpenFFBoard repository](https://github.com/Ultrawipf/OpenFFBoard)
- [Reddit build thread](https://www.reddit.com/r/simracing/comments/1v0l2r9/diy_30nm_openffboard_direct_drive_wheel_with/)
- [Configuration and setup video](https://www.youtube.com/watch?v=Hppz411hfac)

## Pedals

Active force feedback — DIY FFB ActivePedal (cutting edge).

Inspired by commercial active pedals, open-source communities are building force feedback
pedals using small BLDC motors and ball screws. They simulate real ABS pulsing, clutch
bite points, and dynamic brake stiffness driven live by telemetry.

The variant documented here is the mostly 3D-printed design: an iSV57 integrated servo
driving a KK60 ball-screw rail, on a 3060 extrusion base, with PETG-CF structural parts
and TPE vibration-damping adapters.

📋 **[Pedals BOM](./BOM.md#pedals)** · 🔧 **[Build guide](./docs/pedals-build-guide.md)**

### References

- [DIY-Sim-Racing-FFB-Pedal repository](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal)
- [YouTube video explanation](https://www.youtube.com/watch?v=nVImKWnjdjY)
- [Article: this will change the sim racing pedal game](https://simracingcockpit.gg/diy-activepedal-this-will-change-the-sim-racing-pedal-game/)
- [Lebois Racing SRT accelerator pedal](https://lebois-racing.com/srt-accelerator-pedal-p1/)

## Steering Wheel Rim

GT3 style. You can 3D print reinforced wheel plates (using PETG, ABS, or carbon-fiber
composite filament) paired with custom electronics.

- **Designs:** OpenSimRacer, or community CAD files on Thingiverse/Printables for
  Formula 1 or GT3 wheels.
- **MCU:** Arduino Pro Micro or Teensy running SimHub firmware.
- **Display:** 4.3" VoCore screen or Nextion display acting as a live telemetry dash
  (RPM, gear, lap deltas, tire temps).
- **Inputs:** 3D-printed magnetic paddle shifters (neodymium magnets + tactile
  microswitches), rotary encoders, and addressable WS2812B RGB LEDs for shift lights.

📋 **[Wheel rim BOM](./BOM.md#wheel-rim)**

## Shifter

The Lebois Racing SRT (Sim Racing Tech) gearbox is the gold standard for DIY. It is
largely 3D-printed, open-source, features modular tactile resistance, and converts
between H-pattern and sequential modes.

Note that a significant share of the build — custom machined shafts, bearings, magnets
and the PCB — ships as a single Industry&CNC kit rather than as individually sourced
parts; the BOM marks which items those are.

📋 **[Shifter BOM](./BOM.md#shifter)**

### References

- [Lebois Racing](https://lebois-racing.com/)
- [SRT Gearbox V10 documentation](https://lebois-racing.com/srt-gearbox-v10-documentation/)

## Handbrake

3D-printed lever mechanism using an M10 bolt pivot, die springs, and a 20–50 kg load cell
connected via an Arduino for linear handbrake pressure in rally or drift games.

The variant documented in the BOM is the **hydraulic** one: a real single-piston brake
caliper and master cylinder plumbed to a 500 psi pressure transducer, which gives a true
pressure curve rather than a deflection curve.

📋 **[Handbrake BOM](./BOM.md#handbrake)**

### References

- [Hydraulic handbrake P1](https://lebois-racing.com/handbrake-hydraulic-p1/)
- [Lebois Racing](https://lebois-racing.com/)

## Rig Chassis

Avoid 3D printing the structural chassis — it will flex under the force of a direct drive
motor and heavy load-cell braking. Use an 8020 aluminum extrusion frame (4080 / 40160
profiles).

- **3D printed roles:** rig cable clips, button box mounts, mouse/keyboard tray hinges,
  and transducer/bass-shaker mounts.
- **CAD layouts:** OpenSimRacing offers free cutting plans and hardware bills of
  materials.

📋 **[Chassis BOM](./BOM.md#chassis)**

## Repository structure

```
.
├── BOM.md                        # generated — all subsystems + consolidated totals
├── docs/
│   ├── cost-estimate.md          # what the whole setup costs to build
│   └── pedals-build-guide.md     # assembly guide for the 3D-printed FFB pedal
├── src/bom/                      # source of truth: one CSV per subsystem
│   ├── bom-wheelbase.csv
│   ├── bom-pedals.csv
│   ├── bom-wheel-rim.csv
│   ├── bom-shifter.csv
│   ├── bom-handbrake.csv
│   └── bom-chassis.csv
└── tools/
    └── build-bom.py              # regenerates BOM.md from the CSVs
```

Every CSV shares one header:

```csv
subsystem,category,item,part_no,spec,qty,location,notes
```

## Credits

All hardware designs belong to their original authors:

| Project | Author | Used for |
|---|---|---|
| [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard) | Ultrawipf | Wheelbase controller |
| [DIY-Sim-Racing-FFB-Pedal](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal) | ChrGri | Active FFB pedal design, build guide and parts list |
| [Lebois Racing](https://lebois-racing.com/) | Lebois Racing | SRT gearbox, hydraulic handbrake, accelerator pedal |
| OpenSimRacing / OpenSimRacer | community | Chassis cutting plans, wheel rim CAD |

If you are one of these authors and want something changed or removed here, open an issue.

## License

[GPL-3.0](./LICENSE).
