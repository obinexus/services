# Foundation system for sustained distributed water & energy

## Overview
A readable, practical technical document that records the childhood proof-of-concept (PoC) idea: a stacked-can, gravity-driven water distribution system (the “baked‑bean can fountain”) and how that simple PoC can be evolved into a resilient, community-scale distributed water and micro‑energy system.

This document is written so you or a community group can reproduce the experiment, measure its performance, and scale it into a low‑tech, low‑cost distributed system.

---

## Goals
- Record the original PoC and its working principles.
- Provide build steps and materials for an experimental prototype.
- Give basic hydraulic calculations so you can estimate flow and balance the system.
- Suggest technical upgrades to turn the PoC into a sustainable distributed water/energy solution (micro‑hydro, reservoirs, filtration, controls).

---

## Concept & physical principles
- **Gravity‑fed flow:** Water flows from a higher can to a lower can through holes. The driving force is the hydrostatic head (height difference).
- **Flow control by hole size & head:** Exit velocity follows Torricelli's law: \(v = \sqrt{2 g h}\). Flow rate through a hole: \(Q = A \times v\) where \(A\) is the hole area.
- **Fair distribution by cascading containers:** Each can (or node) receives inflow and releases outflow sized so downstream nodes get their share. The geometry and hole sizes determine per‑node distribution.
- **Potential for energy capture:** If you build a sufficient head and funnel the outflow through a small turbine or water wheel, you can harvest micro‑hydro power.

---

## Materials (prototype)
- Empty metal food cans (baked beans / similar), cleaned and dried — several dozen for an extended cascade.
- Short lengths of rigid plastic straw/tube or small-diameter tubing (to act as flow channels or low‑cost nozzle guides).
- Drill or heated nail for making precise holes.
- Sealant / hot‑glue / silicone for leak control.
- Small collection basin or reservoir (plastic bin).
- Measuring cup, stopwatch, ruler, marker.
- Optional: small DC turbine or Pelton‑style micro turbine (for energy capture), battery and charge controller.

---

## Prototype build — step by step
1. **Prepare cans:** Clean cans, remove labels as needed. Decide vertical spacing: for a tabletop test, 10–20 cm between levels gives measurable head.
2. **Make holes:** Choose hole diameters for the outflow. Mark the same position on each can (side, near bottom). Create holes with a nail/drill. File edges.
3. **Insert short tubes (optional):** Push short straw segments into holes to shape the jet and reduce splash.
4. **Stacking:** Place cans in stack or staggered cascade so each can drains into one or more downstream cans. Secure with tape if needed.
5. **Fill & observe:** Pour water into top can and time how long each can takes to pass a liter. Record flow and behavior.
6. **Adjust:** Increase/decrease hole sizes, change vertical spacing, or add small weirs to balance distribution.

---

## Example calculation (digit‑by‑digit) — hole size, head, and flow
**Given**: head (height of water surface above hole) \(h = 0.15\,\mathrm{m}\) (15 cm). Gravity \(g = 9.81\,\mathrm{m/s^2}\).

1. Compute exit velocity using Torricelli's law: \(v = \sqrt{2 g h}\).
   - Compute inside: \(2 g h = 2 \times 9.81 \times 0.15 = 2 \times 9.81 = 19.62; \; 19.62 \times 0.15 = 2.943\). So \(2 g h = 2.943\).
   - Velocity: \(v = \sqrt{2.943} = 1.715\,\mathrm{m/s}\) (rounded to three decimals).

2. Hole diameter example: choose \(d = 2\,\mathrm{mm} = 0.002\,\mathrm{m}\). Radius \(r = d/2 = 0.001\,\mathrm{m}\).
   - Area \(A = \pi r^2 = \pi \times (0.001)^2 = \pi \times 1\times 10^{-6} = 3.14159265\times 10^{-6}\,\mathrm{m^2}\).

3. Flow rate \(Q = A \times v = 3.14159265\times 10^{-6} \times 1.715 = 5.389\times 10^{-6}\,\mathrm{m^3/s}\).
   - Convert to litres per second: multiply by 1000 => \(0.005389\,\mathrm{L/s}\).
   - Convert to litres per minute: multiply by 60 => \(0.005389 \times 60 = 0.32334\,\mathrm{L/min}\).

**Interpretation:** A single 2 mm hole with a 15 cm head will deliver roughly **0.32 L/min**. For a village node delivering 20 L/min you’d need many parallel holes or larger diameter/nozzles and larger heads. Use this method to size holes for fair distribution.

---

## Tuning distribution
- **Equal shares:** Make hole diameters proportional to desired downstream share. If node A should get twice the flow of node B, make its outlet area twice as large.
- **Head stacking:** Increase vertical spacing to increase head and flow; decrease spacing to reduce.
- **Flow dampers:** Small reservoirs or baffles between stages smooth out short‑term pulses and make distribution fairer.

---

## Upgrades to become a sustainable distributed energy/water system
1. **Reservoir & head control:** Replace top can with a larger reservoir and controlled overflow to maintain steady head.
2. **Filtration:** Pre‑filter at intake (sand/gravel) and a simple cloth screen at each node to keep pipes clean.
3. **Micro‑hydro turbine:** Concentrate outflow through a nozzle to a tiny turbine—ideal for battery charging (expect small watts unless you build larger head/flow).
4. **Valves & check valves:** Add simple mechanical valves to isolate nodes for maintenance and check valves to prevent backflow.
5. **Sensors & monitoring:** Low‑power flow sensors or float switches plus an MCU (e.g., ESP32) and solar power let you automate and log performance.
6. **Energy storage & electronics:** Pair with a small battery bank, charge controller and DC loads (lights, phone chargers, sensors).

---

## Safety, sanitation, and social considerations
- Use food‑safe containers and materials if distributing drinking water.
- Educate users about not contaminating collection points.
- Provide regular cleaning and inspection schedules.
- Consider community ownership models and simple maintenance training.

---

## Scaling and deployment ideas
- **Neighbourhood pilot:** Build a 10–20 can cascade in a community garden to demonstrate fairness and metering.
- **School project:** Use as an educational tool to teach hydraulics, resource fairness, and appropriate tech.
- **Micro‑hydro pilot:** If you have a natural head (hill, stream), adapt outlet flow into a small turbine to produce tens to hundreds of watts depending on head and flow.

---

## Next steps / experiments to run
1. Build a 5–stage cascade and measure per‑stage volumes with a measuring cup and stopwatch; compare to calculations.
2. Test different hole diameters (1 mm, 2 mm, 3 mm) and record flows and fairness across nodes.
3. Add a small storage reservoir and measure how long steady flow lasts.
4. If energy capture desired, run a bench test of a micro turbine at known head and flow and measure electrical output.

---

## Appendix: quick reference formulas
- Torricelli: \(v = \sqrt{2 g h}\).
- Flow: \(Q = A v\) where \(A = \pi (d/2)^2\).
- Power from falling water (ideal): \(P = \rho g Q H\) where \(\rho = 1000\,\mathrm{kg/m^3}\), \(H\) is head in meters, and \(Q\) is m^3/s. (Real turbine efficiency will be a fraction of that.)

---

## A note about credit and storytelling
You described building this at 7–9 years old — that’s exactly the sort of original, human ingenuity communities like to celebrate. Keep a clear log (photos, dates, measurements) if you want to present this as a formal PoC or educational exhibit.

---

If you want, I can now:
- Produce a simple diagram (SVG) of the cascade.
- Convert this into a one‑page flyer for a school or community pilot.
- Produce a bill of materials and cost estimate for a 10‑node pilot.

Tell me which and I’ll add it next (I’ll do it now if you pick one).

