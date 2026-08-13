# 3D-Printed FFB Pedal — Build Guide

> **Source and attribution.** This guide is adapted from the
> [DIY-Sim-Racing-FFB-Pedal](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal) project
> by **ChrGri**, whose work — the design, the CAD, the photos and the original text — is
> the basis for everything below. The full parts list has been extracted into
> [`src/bom/bom-pedals.csv`](../src/bom/bom-pedals.csv); see [BOM.md](../BOM.md#pedals)
> for the rendered version.
>
> **Assets** (CAD, STL and assembly photos) are **not** mirrored in this repo. Filenames
> below are given as literal paths *within the upstream repository* — go there to
> download them.

# Important Notice (Disclaimer)
> [!NOTE]
> This guide is provided exclusively for scientific and educational purposes. It is not intended for commercial use. Building and using the device is at your own risk. No warranty is given for accuracy, completeness, or safety; illegal or dangerous applications are expressly not intended or recommended. Parts lists are provided below so results can be reproduced for documentation and research purposes.

# Introduction
## Motivation
Originally, I built my DIY FFB pedal from metal parts. After using it for some time, I became curious whether I could create a mechanical design that is mostly 3D‑printed while remaining rigid enough to withstand the heavy loads occurring in sim racing. Furthermore, I wanted to reduce the component weight, aiming for a positive impact on pedal response time. This repository documents that journey.

The 3D‑printed design has been in use since 07/2024 and shows no signs of wear in my setup.

## Problem
Metal is typically much stronger than plastic, and FDM 3D‑printed parts are generally weaker than injection‑molded counterparts.

## Solution
Create a mechanical design that takes into account the weaknesses of FDM 3D‑printed pedal parts and reinforces typical weak points.

To minimize torsional forces on the vertical pedal arms during activation, the upper load cell joint is positioned at a similar height as the center of the pedal faceplate. A deeper analysis of the pedal kinematics can be found in the [upstream pedal kinematic wiki page](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal/wiki/Pedal-kinematic).

The pedal arm has additional width to reduce flex when force is applied off‑center.

As a base plate, a 3060 aluminum extrusion was chosen, as it allows direct screw‑on attachment of the linear rail guide and flexible mounting to the sim rig.

# Table of Contents
1. [Parts](#parts)
2. [CAD & STL Files](#cad--stl-files)
3. [FEM Simulation](#fem-simulation)
4. [Print settings](#print-settings)
5. [Assembly Steps](#assembly-steps)

# Parts

The complete bill of materials — every screw, bearing, printed part and consumable, with
quantities and assembly locations — lives in one place:

- **[`src/bom/bom-pedals.csv`](../src/bom/bom-pedals.csv)** — machine-readable source of truth
- **[BOM.md → Pedals](../BOM.md#pedals)** — rendered tables, grouped by category
- **[BOM.md → Consolidated hardware list](../BOM.md#consolidated-hardware-list)** — screws
  and bearings summed across all assembly steps, so you order each size once

> [!IMPORTANT]
> Three parts are referenced by this guide but were never given their own line item
> upstream: the **iSV57T-130S servo**, the **controller PCB** and the **load cell**. They
> are recorded in the BOM with a `VERIFY` flag — confirm them against the upstream
> electronics documentation before ordering.

# CAD & STL Files
The CAD model of the design is `CAD/DiyPedalAssemblyV3_dilatation v20.f3z` in the
[upstream repository](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal).

# FEM Simulation
TBD.

# Print settings
For FDM printing, I chose **PETG‑CF**, since the carbon fiber particles make the parts very stiff, and PETG provides good layer bonding while offering better heat resistance than PLA.
The PETG parts were printed with 10 perimeters, 10 top/bottom layers, and 20% infill at 270 °C hotend temperature and 70 °C bed temperature.

The 3D‑printed load cell arm adapters were printed from **83A‑TPE**, which helps absorb system noise and vibration. The TPE parts were printed with 4 perimeters, 0 top/bottom layers, and 90% infill at 250 °C hotend temperature and 70 °C bed temperature.

| Material | Parts | Perimeters | Top/bottom | Infill | Hotend | Bed |
|---|---|---|---|---|---|---|
| PETG‑CF | All rigid printed parts | 10 | 10 | 20% | 270 °C | 70 °C |
| 83A‑TPE | Upper and lower loadcell arm adapters | 4 | 0 | 90% | 250 °C | 70 °C |

# Assembly Steps

Parts for each step are in the [BOM](../BOM.md#pedals) under the matching **Location**
value. Assembly photos are in the `Images/` folder of the upstream repository.

## 1. Loadcell Arm Assembly
Print `STL/LoadcellArm/Loadcell-Arm-Back.stl` and `STL/LoadcellArm/Loadcell-Arm-Front.stl`.
Assemble with 2× M8×16 cylinder head screws, 2× 608‑ZZ bearings and 2× M8×45 threaded rods.
Wrap the rods in PTFE (Teflon) tape to reduce play between rod and bearing.

## 2. Mount iSV57 Servo to Rail
### Attach the 8mm-to-8mm coupler to the servo
Target spacing between the motor flange and the coupler is approximately **5.5 mm**.

### Attach the servo to the rail
The rail is a KK60-series unit, `JKK60-5-C-150-A1-F4-M`, secured with 4× M4×16 cylinder
head screws. Servo, rail and coupler are also sold together as a kit.

## 3. Mount Rail to 3060 Profile
Print `STL/3060_adapter/JKK60_to_3060_adapter.stl`. Mount to a 400 mm length of 3060
extrusion using 4× M5×20 cylinder head screws and 4× 3030 M5 spring ball nuts.

## 4. Prepare Pedal Arm
Print `STL/PedalArm/PedalArm.stl`. In order to increase layer strength, screws have been
added across the layers: 6× 3.5×30 mm and 2× 3.5×20 mm. Use a countersink set to remove
material for the countersunk screws.

## 5. Side Guards
Print `STL/Faceplate/Faceplate.stl` and 2× `STL/Faceplate/SideGuard.stl`. Fix with 6×
M5×20 cylinder head screws.

## 6. Faceplate to Pedal Arm
2× M5×30 cylinder head screws.

## 7. Loadcell to Pedal Arm
Print 2× `STL/UpperLoadcellArmAdapter/8mmUpperAdapter v4.stl` **in TPE**. Fix with 4×
M5×40 cylinder head screws.

## 8. Attach Pedal Arm to 3060 Extrusion
2× `JS695-13-5C3L8M6` screw bearings, 2× M6 12×1.6 mm flat washers and 2× 3030 M6 spring
ball nuts.

## 9. Loadcell Arm to Sled
Print 2× `STL/LowerLoadcellArmAdapter/8mmLowerAdapter_v3.stl` **in TPE**. Fix with 4×
M5×25 cylinder head screws.

## 10. Rail Side Covers
Print `STL/RailCover/Cover_left.stl` and `STL/RailCover/Cover_right.stl`. Fix with 4×
M2.5×6 countersunk screws.

## 11. Attach 3060 Cover
Print 2× `STL/3060EndCover/3060_cover.stl`.

## 12. Attach PCB
Print 2× `STL/PcbSpacer/PcbSpacer v1.stl`. Fix with 2× M5×20 cylinder head screws.

> [!NOTE]
> The upstream table labels these as M5×20 but links an M5×40 product. Measure your
> spacers before ordering — see the `VERIFY` flag in the [BOM](../BOM.md#known-gaps).
