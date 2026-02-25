# site_config.py
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class SiteConfig:
  image_filename: str = "man-performing-emergency-maintenance.webp"  # sits next to generate.py

  # Identity
  base_name: str = "Emergency Maintenance"
  brand_name: str = "Emergency Maintenance Experts"

  # Pricing base
  cost_low: int = 350
  cost_high: int = 8500

  # Core titles/subs
  h1_title: str = "Emergency Maintenance/24 Hour Maintenance Services"
  h1_short: str = "Emergency Maintenance Services"

  cost_title: str = "Emergency Maintenance Cost"
  howto_title: str = "How Emergency Maintenance Works"

  about_blurb: str = (
    "We provide emergency maintenance services{loc} for urgent, unplanned property issues that pose safety risks or can cause serious damage. "
    "Our team responds to critical problems like active water leaks, gas concerns, total service outages, and plumbing failures to stabilize conditions quickly. "
    "Use our 24-hour emergency maintenance service to get fast response when immediate action is required."
  )


  # MAIN PAGE
  main_h2: tuple[str, ...] = (
    "What Is Considered Emergency Maintenance in an Apartment?",
    "What Are Common Emergency Maintenance Examples?",
    "Is No Hot Water a Maintenance Emergency?",
    "Is No AC Considered a Maintenance Emergency?",
    "Is an Emergency Water Leak Repair Considered Emergency Maintenance?",
    "What Should You Do If Apartment Emergency Maintenance Is Not Answering?",
  )

  main_p: tuple[str, ...] = (
    "Emergency maintenance refers to urgent, unplanned repairs that must be handled immediately to prevent safety hazards, health risks, or serious property damage. These situations typically involve gas leaks, major water leaks, electrical hazards, or loss of essential services that make a unit unsafe or unlivable.",
    "Common emergency maintenance situations include active flooding, sewage backups, gas odors, sparking electrical outlets, total power loss, and heating failures during freezing temperatures. If the issue threatens safety or can cause rapid damage, it’s usually considered an emergency.",
    "No hot water can be an emergency when it affects basic sanitation, is building-wide, or is caused by a serious system failure. In colder climates or when paired with leaks or electrical issues, loss of hot water may require immediate response.",
    "No air conditioning can be considered a maintenance emergency when indoor temperatures create health or safety risks, especially during extreme heat. In hot climates or heat wave conditions, loss of AC may require immediate attention, while mild weather situations may be handled through standard maintenance scheduling.",
    "Yes, emergency water leak repair is a core part of emergency maintenance because uncontrolled leaks can quickly damage walls, floors, and electrical systems. Active leaks from ceilings, pipes, or fixtures should be reported immediately using emergency maintenance channels.",
    "If apartment emergency maintenance is not answering, tenants should document the issue and contact property management through all designated emergency methods. For immediate safety threats such as gas smells, flooding, or electrical danger, contacting emergency services or the utility provider may be necessary."
  )


  # LOCAL COST
  location_cost_h2: str = "How Much Does Emergency Maintenance Cost{loc}?"
  location_cost_p: str = (
    "Emergency maintenance costs{loc} typically range between {cost_lo} and {cost_hi}, and depend on the type of issue and time of day. "
    "Pricing can also vary based on after-hours labor rates, parts required, and whether the visit involves leak mitigation or other urgent repairs."
  )

  # Meta descriptions (keep them unique per page, ~150-160 chars)
  home_description: str = (
    "24-hour emergency maintenance for urgent property issues like leaks, no hot water, and broken toilets. Fast response and damage control."
  )

  city_description: str = (
    "Emergency maintenance services{loc} for leaks, no hot water, clogged toilets, and urgent repairs. 24-hour availability and fast response."
  )

  cost_description: str = (
    "Emergency maintenance cost guide: typical pricing ranges, after-hours factors, and what affects total cost for urgent repairs."
  )

  cost_city_description: str = (
    "Emergency maintenance cost{loc}: typical local pricing ranges and factors like after-hours response, parts, and repair scope."
  )

  howto_description: str = (
    "How emergency maintenance works: what qualifies as an emergency, common examples, and what to expect during urgent repair response."
  )

  contact_description: str = (
    "Request emergency maintenance service. Share your location and the issue details to get fast scheduling and urgent repair help."
  )

  state_description: str = (
    "Emergency maintenance services{loc}. Browse cities we serve, view typical pricing ranges, and request urgent repair help."
  )

  networx_embed = """
  <div id="networx_form_container" style="margin:0px;padding:0px;">
      <div id = "nx_form" style = "width: 242px; height: 375px;">
          <script type="text/javascript" src = "https://api.networx.com/iframe.php?aff_id=73601bc3bd5a961a61a973e92e29f169&aff_to_form_id=8030"></script>
      </div>
  </div>
  """


  cost_body = """
  <section>
    <h2>Antenna Removal Cost Ranges (Most Common Scenarios)</h2>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Removal Scenario</th>
            <th>Typical Cost Range</th>
            <th>What You’re Paying For</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Remove small TV antenna (single-story roof)</td>
            <td>$100–$250</td>
            <td>Antenna detachment, basic hardware removal</td>
          </tr>
          <tr>
            <td>Remove roof-mounted TV antenna (two-story home)</td>
            <td>$200–$450</td>
            <td>Roof access, safe removal, hardware disassembly</td>
          </tr>
          <tr>
            <td>Remove large or older rooftop antenna (tower-style)</td>
            <td>$300–$800</td>
            <td>Multi-section dismantling, controlled lowering</td>
          </tr>
          <tr>
            <td>Remove antenna mast and mounting brackets</td>
            <td>$150–$400</td>
            <td>Mast removal, bracket extraction, fastener cleanup</td>
          </tr>
          <tr>
            <td>Patch and seal roof penetrations</td>
            <td>$150–$500</td>
            <td>Flashing repair, sealant, leak prevention</td>
          </tr>
          <tr>
            <td>Interior cable removal (optional)</td>
            <td>$100–$300</td>
            <td>Disconnect and remove visible antenna cabling</td>
          </tr>
          <tr>
            <td>High access or steep roof work</td>
            <td>+20% to +50%</td>
            <td>Safety setup, ladders, harnesses, or lift</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      <strong>Typical total:</strong> $150–$450 for most residential antenna removals.
      <strong>Large or high-access antennas:</strong> $800+ is possible.
    </p>

    <hr />

    <h2>Cost by Severity (Fast Self-Assessment)</h2>

    <h3>Minor</h3>
    <ul>
      <li><strong>What it looks like:</strong> small TV antenna, easy roof access</li>
      <li><strong>Expected cost:</strong> $100–$250</li>
      <li><strong>Common work:</strong> detach antenna and remove base hardware</li>
    </ul>

    <h3>Moderate</h3>
    <ul>
      <li><strong>What it looks like:</strong> roof-mounted antenna with mast and brackets</li>
      <li><strong>Expected cost:</strong> $250–$450</li>
      <li><strong>Common work:</strong> mast removal + roof hardware extraction</li>
    </ul>

    <h3>Severe</h3>
    <ul>
      <li><strong>What it looks like:</strong> large, old, or tower-style antenna; steep or tall roof</li>
      <li><strong>Expected cost:</strong> $450–$800+</li>
      <li><strong>Common work:</strong> multi-section dismantling + roof repair</li>
    </ul>

    <hr />

    <h2>Antenna Removal Cost by Installation Type</h2>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Antenna Type</th>
            <th>Typical Removal Range</th>
            <th>Why It Costs More (or Less)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Small TV antenna</td>
            <td>$100–$250</td>
            <td>Lightweight, minimal mounting hardware</td>
          </tr>
          <tr>
            <td>Roof-mounted antenna with mast</td>
            <td>$200–$450</td>
            <td>More fasteners and roof penetrations</td>
          </tr>
          <tr>
            <td>Large rooftop or attic-fed antenna</td>
            <td>$300–$800+</td>
            <td>Heavier sections and careful lowering required</td>
          </tr>
          <tr>
            <td>Tower-style or multi-section antenna</td>
            <td>$500–$1,500+</td>
            <td>Complex dismantling and safety considerations</td>
          </tr>
        </tbody>
      </table>
    </div>

    <hr />

    <h2>What Increases Antenna Removal Cost</h2>

    <ul>
      <li><strong>Roof height:</strong> two-story or taller homes increase labor and safety needs</li>
      <li><strong>Roof pitch:</strong> steep roofs slow work and require harnesses</li>
      <li><strong>Antenna size:</strong> larger or older antennas take longer to dismantle</li>
      <li><strong>Mounting method:</strong> lag bolts, brackets, or concrete bases add time</li>
      <li><strong>Roof repair:</strong> sealing holes and flashing adds scope</li>
      <li><strong>Disposal:</strong> hauling and recycling metal components</li>
    </ul>

    <hr />

    <h2>When Simple Removal Is Enough vs When Roof Repair Is Required</h2>

    <h3>Simple removal is usually enough if:</h3>
    <ul>
      <li>The antenna is surface-mounted with minimal penetrations</li>
      <li>Fasteners can be removed cleanly</li>
      <li>No water staining or soft roof decking is present</li>
    </ul>

    <h3>Roof repair is usually required if:</h3>
    <ul>
      <li>Lag bolts or mounts penetrated shingles or roofing membrane</li>
      <li>Sealant has failed or cracked over time</li>
      <li>There are visible holes, rust stains, or water intrusion</li>
    </ul>

    <p>
      <strong>Rule:</strong> If mounting hardware penetrated the roof, sealing and flashing should be included — not optional.
    </p>

    <hr />

    <h2>Common Add-Ons During Antenna Removal</h2>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Add-On</th>
            <th>Typical Cost</th>
            <th>Best Use</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Roof hole patching and sealing</td>
            <td>$150–$500</td>
            <td>Prevents leaks after removal</td>
          </tr>
          <tr>
            <td>Complete cable removal</td>
            <td>$100–$300</td>
            <td>Eliminates unused interior/exterior wiring</td>
          </tr>
          <tr>
            <td>Metal disposal or recycling</td>
            <td>$50–$150</td>
            <td>Proper handling of old antenna materials</td>
          </tr>
          <tr>
            <td>Paint or cosmetic touch-up</td>
            <td>$100–$400</td>
            <td>Hides old mounting marks</td>
          </tr>
        </tbody>
      </table>
    </div>

    <hr />

    <h2>What an Antenna Removal Quote Should Include</h2>

    <ul>
      <li>Antenna size, type, and mounting method</li>
      <li>Roof height and pitch</li>
      <li>Mast and bracket removal scope</li>
      <li>Roof sealing or flashing plan</li>
      <li>Disposal or recycling of removed materials</li>
      <li>Access method and safety setup</li>
    </ul>

    <hr />

    <h2>Insurance and Property Considerations</h2>

    <p>
      Antenna removal is typically considered maintenance, not an insurance claim.
      If removal is due to storm damage, limited coverage may apply.
      Always address roof penetrations immediately to avoid future leaks.
    </p>
  </section>
  """

  howto_body = """
  <section>
    <p>
      Removing an antenna involves more than unbolting hardware. Improper removal can damage roofing, siding, or structural framing and create active leak points if not sealed correctly.
    </p>

    <p>
      This guide explains how to remove an antenna step by step, including safety precautions, disconnection methods, mounting removal, and proper sealing to protect the structure afterward.
    </p>
    <h2>Step 1: Identify the Antenna Type and Mounting Method</h2>

    <p>
      Before removal, determine how the antenna is installed and what it is attached to.
    </p>

    <h3>Common antenna types include:</h3>
    <ul>
      <li>Roof-mounted television antennas</li>
      <li>Mast-mounted antennas attached to fascia or gable ends</li>
      <li>Chimney-mounted antennas with strap kits</li>
      <li>Interior or attic-mounted antennas</li>
    </ul>

    <h3>Confirm how the antenna is supported:</h3>
    <ul>
      <li>Lag bolts into rafters or framing</li>
      <li>Mounting brackets fastened through roofing</li>
      <li>Straps or bands around masonry chimneys</li>
    </ul>

    <p>
      Never begin removal without understanding what structural elements are involved.
    </p>

    <hr />

    <h2>Step 2: Disconnect Power and Signal Cables</h2>

    <p>
      Antennas are typically connected to coaxial, grounding, or amplifier wiring that must be safely removed first.
    </p>

    <ol>
      <li>Disconnect coaxial cables from interior equipment</li>
      <li>Trace and free exterior cabling from clips or conduit</li>
      <li>Remove grounding wires bonded to electrical ground or rods</li>
      <li>Cap or remove unused wall penetrations</li>
    </ol>

    <p>
      Some antennas include powered amplifiers. Verify all power sources are disconnected before proceeding.
    </p>

    <hr />

    <h2>Step 3: Safely Remove the Antenna and Mast</h2>

    <h3>Roof or Mast-Mounted Antennas</h3>
    <ol>
      <li>Use proper fall protection and stable ladder access</li>
      <li>Loosen mounting hardware while supporting the mast</li>
      <li>Lower the antenna assembly carefully to the ground</li>
    </ol>

    <h3>Chimney-Mounted Antennas</h3>
    <ol>
      <li>Cut or loosen metal strap kits evenly</li>
      <li>Prevent sudden release that could damage masonry</li>
      <li>Lower the antenna in sections if needed</li>
    </ol>

    <p>
      Antennas can be top-heavy and awkward. Never attempt removal alone if the assembly is large.
    </p>

    <hr />

    <h2>Step 4: Remove Mounting Hardware</h2>

    <ol>
      <li>Extract lag bolts, brackets, and flashing</li>
      <li>Inspect roof decking, siding, or framing for damage</li>
      <li>Remove abandoned anchors or fasteners</li>
    </ol>

    <p>
      Leaving hardware behind often leads to leaks, corrosion, or future structural issues.
    </p>

    <hr />

    <h2>Step 5: Seal and Repair the Installation Area</h2>

    <ul>
      <li>Fill all bolt holes with exterior-grade sealant or epoxy</li>
      <li>Replace or repair damaged shingles or siding</li>
      <li>Install proper flashing where roof penetrations existed</li>
      <li>Prime and paint exposed materials as needed</li>
    </ul>

    <p>
      Proper sealing is the most critical step in preventing long-term water damage.
    </p>

    <hr />

    <h2>When to Hire a Professional</h2>

    <ul>
      <li>Antennas mounted high or over steep roof pitches</li>
      <li>Penetrations through finished roofing systems</li>
      <li>Structural or chimney-mounted installations</li>
      <li>Evidence of existing leaks or rot</li>
    </ul>

    <p>
      Professional removal reduces the risk of falls, roof damage, and improper sealing.
    </p>
  </section>
  """

CONFIG = SiteConfig()