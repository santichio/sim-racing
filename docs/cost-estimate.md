# Cost Estimate

What this setup costs to build, per subsystem and in total.

> [!IMPORTANT]
> **None of these numbers come from the BOM.** The CSVs in [`src/bom/`](../src/bom)
> carry no price data — the upstream sources were priced through affiliate links that
> have since rotted, and guessing values into the parts lists would break the repo's
> "nothing here is guessed" rule. Everything below is a **hand-made market estimate**
> (street prices, 2025–2026, EUR; USD lands within roughly 10%). Treat it as a
> budgeting aid, not a quote.

Two variables move the total more than anything else:

- **Where you buy.** Chinese direct (AliExpress) versus EU/US-stocked distributors is
  close to a 2× spread on the servo motors, ball-screw rails and extrusion.
- **How many active pedals you build.** The [pedal BOM](../BOM.md#pedals) describes
  **one** pedal. A brake-only build is a third of the cost of throttle + brake + clutch.

## Contents

- [Per subsystem](#per-subsystem)
- [Totals](#totals)
- [Costs the BOM does not capture](#costs-the-bom-does-not-capture)
- [Confidence](#confidence)

<a id="per-subsystem"></a>

## Per subsystem

| Subsystem | Lean | Mid | High | Main cost driver |
|---|---:|---:|---:|---|
| [Wheelbase](../BOM.md#wheelbase) | €520 | €800 | €1,200 | `130ST-M10010` (10 Nm) ≈ €200–300 vs. `130ST-M15015` (20–30 Nm) ≈ €300–450, usually kitted with the `AASD-15A` driver. OpenFFBoard: ≈ €60 self-assembled, ≈ €250 bought built |
| [Pedals](../BOM.md#pedals) — per pedal | €330 | €400 | €480 | `iSV57T-130S` ≈ €100–140; `JKK60` ball-screw rail ≈ €120–200 as a clone, €300+ genuine Hiwin |
| → throttle + brake (2×) | €660 | €800 | €960 | |
| → throttle + brake + clutch (3×) | €990 | €1,200 | €1,440 | |
| [Steering wheel rim](../BOM.md#wheel-rim) | €150 | €230 | €300 | VoCore 4.3" ≈ €70–90 vs. Nextion ≈ €45; Pro Micro ≈ €8 vs. Teensy ≈ €25; wheel-side quick release €30–80 |
| [Shifter](../BOM.md#shifter) | €230 | €290 | €350 | The Industry&CNC machined kit + PCB is most of the total (≈ €130–200); 1.3 kg of PLA ≈ €30 |
| [Handbrake](../BOM.md#handbrake) | €130 | €190 | €250 | Caliper + master cylinder set €40–80; 500 psi transducer €15–30; lever assembly €30–80 |
| [Rig chassis](../BOM.md#chassis) | €500 | €700 | €950 | ≈ 10–14 m of extrusion at €25–35/m (4080) and €50–70/m (40160), plus €80–150 in brackets and T-nuts |
| Seat + brackets | €150 | €250 | €450 | Not in any BOM — see [below](#costs-the-bom-does-not-capture) |

<a id="totals"></a>

## Totals

| Build | Spec | Total |
|---|---|---:|
| **Lean** | 10 Nm motor, 2 active pedals, sourced direct from China | **≈ €2,350** |
| **Mid** | 20 Nm motor, 3 active pedals | **≈ €3,600** |
| **High** | EU-sourced parts, genuine rails, larger frame | **≈ €4,900** |

Add **10–15% for consumables, spares and rework** — PETG-CF at ≈ €35/kg, TPE, the
fasteners you sized wrong, the board you let the smoke out of. If you are importing into
the EU, **VAT and duty apply on top of the sticker price**, which alone pushes the mid
build past €4,200.

<a id="costs-the-bom-does-not-capture"></a>

## Costs the BOM does not capture

These are real gaps rather than padding — parts the build needs that no upstream source
enumerated:

| Item | Estimate | Why it is missing |
|---|---:|---|
| 24–48 V DC power supply for the pedal servos | €30–60 | The `iSV57T-130S` needs one; no CSV lists it |
| Wheelbase motor mount plate | €50–120 | Machined or laser-cut steel. The BOM only covers the *printed* parts |
| Motor shaft hub / quick release | €40–120 | The BOM lists the printed locking ring, not the QR itself |
| Seat, sliders and seat brackets | €150–450 | Outside every upstream parts list |
| A 3D printer that can run PETG-CF | €250–800 | Needs a hardened nozzle; ≈ 1.5 kg of print across the whole build |
| PC, monitors or VR headset | — | Out of scope for this repo |

<a id="confidence"></a>

## Confidence

The **wheelbase** and **chassis** figures are the softest. Both CSVs are marked
*Skeleton* in the [README](../README.md#bill-of-materials): no motor variant is chosen,
no extrusion lengths or quantities are recorded. Those two rows price a *typical* build,
not a specific one.

Resolving the entries in [Known gaps](../BOM.md#known-gaps) — motor and driver choice
first, then the extrusion cutting list — would tighten the whole estimate to roughly
±10%.
