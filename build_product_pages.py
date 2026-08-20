#!/usr/bin/env python3
"""Generate the Modern Home Blinds product pages.

Each page reuses the shared design system in assets/product.css and the
nav / footer markup from the homepage (index.html). Content is defined in
PRODUCTS below so the pages stay consistent and easy to update.
"""
import html

PHONE = "647-673-1847"
PHONE_TEL = "6476731847"
EMAIL = "wahhab2020@gmail.com"

# ── Shared product catalogue (slug -> short name) for nav / related ──────────
CATALOG = [
    ("zebra-blinds", "Zebra Blinds"),
    ("roller-shades", "Roller Shades"),
    ("roman-shades", "Roman Shades"),
    ("cellular-shades", "Cellular Shades"),
    ("skylight-cellular-blinds", "Skylight Cellular Blinds"),
    ("silhouette-shades", "Silhouette Shades"),
    ("soft-vertical-blinds", "Vertical Blinds"),
    ("faux-wood-blinds", "Faux Wood Blinds"),
    ("california-shutters", "California Shutters"),
    ("wood-california-shutters", "Wood California Shutters"),
    ("vinyl-california-shutters", "Vinyl California Shutters"),
    ("draperies-sheers", "Draperies & Sheers"),
    ("outdoor-patio-awnings", "Outdoor Patio Awnings"),
    ("smart-film", "Smart Film"),
    ("motorized-blinds", "Motorized Blinds"),
]

# image key per slug
IMG = {
    "zebra-blinds": "prod-zebra.jpg",
    "roller-shades": "prod-roller.jpg",
    "roman-shades": "prod-roman.jpg",
    "california-shutters": "prod-california.jpg",
    "silhouette-shades": "prod-silhouette.jpg",
    "cellular-shades": "prod-cellular.jpg",
    "draperies-sheers": "prod-draperies.jpg",
    "motorized-blinds": "prod-motorized.jpg",
    "soft-vertical-blinds": "prod-vertical.jpg",
    "wood-california-shutters": "prod-california.jpg",
    "vinyl-california-shutters": "prod-california.jpg",
    "faux-wood-blinds": "prod-california.jpg",
    "outdoor-patio-awnings": "prod-vertical.jpg",
    "skylight-cellular-blinds": "prod-cellular.jpg",
    "smart-film": "prod-motorized.jpg",
}

PRODUCTS = {
    "zebra-blinds": dict(
        name="Zebra Blinds",
        h1=("Custom <em>Zebra Blinds</em> in the GTA"),
        pill="Most Popular",
        title="Zebra Blinds GTA | Custom Day & Night Blinds — Modern Home Blinds",
        desc="Custom zebra (day & night) blinds manufactured in Oakville. Alternating sheer and solid bands for effortless light control and privacy. Free in-home consultation across the GTA.",
        sub="Alternating sheer and solid fabric bands glide past each other so you can dial in the perfect balance of light, view and privacy — all from a single, elegant shade.",
        price=(190, 290),
        ov_title="The most versatile shade we make",
        ov_p=[
            "Zebra blinds — also called day &amp; night or dual shades — pair sheer and opaque fabric bands on a single roller. Align the bands for an open, airy view, or stagger them to filter light and gain full privacy. It is the reason they are our single most requested product across the GTA.",
            "Every zebra blind is cut, assembled and quality-checked in our Oakville workshop, then installed by our own team. No middle-men, no big-box markups — just a precision fit for your windows.",
        ],
        bullets=[
            ("Infinite light control", "Slide the bands to move seamlessly from sheer daylight to full privacy."),
            ("Clean, modern look", "Slim cassette headrail and crisp banding suit contemporary GTA homes and condos."),
            ("Easy to live with", "Wipe-clean fabrics and a smooth chain or motorized lift built for daily use."),
            ("Made & installed locally", "Manufactured in Oakville and professionally installed — usually within a week."),
        ],
        benefits=[
            ("&#9728;", "Light Control", "Two-in-one sheer and solid bands let you fine-tune brightness without ever swapping shades."),
            ("&#128274;", "Privacy On Demand", "Close the solid bands for complete privacy at night while keeping a soft, finished look."),
            ("&#10024;", "Aesthetic Appeal", "A sleek, layered fabric design that instantly modernises any room."),
            ("&#128170;", "Durability", "Premium fade-resistant fabrics and quality components built to last for years."),
            ("&#128176;", "Great Value", "Designer style and function at a price that beats the big retailers."),
            ("&#9881;", "Motorized Option", "Add quiet motorization with remote, app and voice control."),
        ],
        specs=[("100+", "Fabric &amp; colour options"), ("1 wk", "Typical install time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Kitchen"), ("&#128716;", "Bedroom"),
               ("&#127968;", "Home Office"), ("&#128701;", "Bathroom"), ("&#127970;", "Condos"),
               ("&#127797;", "Sunrooms"), ("&#127859;", "Dining Room")],
        faqs=[
            ("What exactly are zebra blinds?", "Zebra blinds combine alternating sheer and solid horizontal fabric bands on one roller mechanism. As you raise or lower the shade the bands shift, letting you switch between a clear view, filtered light, or full privacy."),
            ("Do zebra blinds give full privacy at night?", "Yes. When the solid bands are aligned they block the view inside. For bedrooms or street-facing windows we can also pair them with a blackout roller for total darkness."),
            ("Can zebra blinds be motorized?", "Absolutely. We offer quiet motors with remote, smartphone app and voice control (Alexa, Google Home, Apple HomeKit) — perfect for large or hard-to-reach windows."),
            ("How much do zebra blinds cost?", "Most zebra blinds land between $190 and $290 per window installed, depending on size and fabric. Your free in-home measurement confirms exact pricing with no obligation."),
        ],
    ),
    "roller-shades": dict(
        name="Roller Shades",
        h1=("Custom <em>Roller Shades</em> for Every Window"),
        pill="Clean & Minimal",
        title="Roller Shades GTA | Custom Blackout & Solar Shades — Modern Home Blinds",
        desc="Custom roller shades manufactured in Oakville — light-filtering, blackout and solar-screen fabrics. Clean, minimal styling with motorized options. Free GTA consultation.",
        sub="A single, smooth panel of fabric that disappears into a slim cassette. Choose light-filtering, blackout or solar-screen fabrics to suit every room.",
        price=(160, 260),
        ov_title="Simple, refined and endlessly practical",
        ov_p=[
            "Roller shades are the workhorse of modern window covering — uncomplicated, durable and available in hundreds of fabrics. Pick a light-filtering weave for a soft glow, a blackout fabric for bedrooms and media rooms, or a solar screen that cuts glare while keeping your view.",
            "Ours are made to measure in Oakville with a clean reverse-roll cassette that hides the tube and hardware for a tidy, architectural finish.",
        ],
        bullets=[
            ("Three fabric families", "Light-filtering, blackout and solar-screen options for any room."),
            ("Minimal footprint", "A slim cassette keeps the look clean and contemporary."),
            ("Low maintenance", "Smooth, wipeable fabrics that resist dust and fading."),
            ("Motor-ready", "Upgrade to motorization for one-touch or scheduled control."),
        ],
        benefits=[
            ("&#10024;", "Modern Finish", "A flush, minimal profile that complements any contemporary interior."),
            ("&#9202;", "Timeless Design", "A classic, uncluttered look that never goes out of style."),
            ("&#9728;", "Easy Light Control", "Set the shade anywhere for the exact light level you want."),
            ("&#129529;", "Low Maintenance", "Durable fabrics wipe clean and stay looking new."),
            ("&#9881;", "Motorized Option", "Add quiet motorization with remote, app and voice control."),
            ("&#127759;", "Solar Screen Choice", "Block UV and glare while keeping your outdoor view."),
        ],
        specs=[("150+", "Fabric &amp; colour options"), ("1 wk", "Typical install time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Kitchen"), ("&#128716;", "Bedroom"),
               ("&#127902;", "Media Room"), ("&#128701;", "Bathroom"), ("&#127970;", "Condos"),
               ("&#127968;", "Home Office"), ("&#127797;", "Sunrooms")],
        faqs=[
            ("What is the difference between light-filtering and blackout roller shades?", "Light-filtering fabrics soften and diffuse daylight while keeping the room bright. Blackout fabrics block virtually all light — ideal for bedrooms, nurseries and media rooms."),
            ("What are solar roller shades?", "Solar (sunscreen) shades use an open-weave fabric that blocks UV rays and glare while preserving your outdoor view. They are great for sun-facing windows and home offices."),
            ("Can roller shades be motorized?", "Yes — our roller shades accept quiet motors controlled by remote, smartphone app, schedules, or voice assistants."),
            ("How much do roller shades cost?", "Roller shades typically run $160 to $260 per window installed depending on fabric and size. Your free in-home measurement gives you an exact quote."),
        ],
    ),
    "roman-shades": dict(
        name="Roman Shades",
        h1=("Custom <em>Roman Shades</em> — Soft, Tailored Elegance"),
        pill="Tailored & Elegant",
        title="Roman Shades GTA | Custom Fabric Roman Blinds — Modern Home Blinds",
        desc="Custom Roman shades manufactured in Oakville. Soft fabric folds, child-safe lifts and premium materials. Timeless, tailored window styling across the GTA.",
        sub="Luxurious fabric that stacks into soft, even folds as it rises and drapes flat when lowered — the warmth of drapery with the function of a shade.",
        price=(240, 420),
        ov_title="The warmth of fabric, tailored to your window",
        ov_p=[
            "Roman shades bring softness and texture that hard blinds simply can't. When raised they gather into neat horizontal folds; when lowered they fall into a smooth, elegant panel. The result is a high-end, decorator look that feels at home in both traditional and modern interiors.",
            "We sew each Roman shade to your exact measurements in Oakville, with your choice of fabric, lining and a child-safe cordless or motorized lift.",
        ],
        bullets=[
            ("Hand-sewn to size", "Tailored from your chosen fabric for a flawless, custom fit."),
            ("Choice of lining", "Add privacy, blackout or thermal lining for extra performance."),
            ("Child-safe lifts", "Cordless and motorized options keep homes with kids and pets safe."),
            ("Designer fabrics", "Hundreds of premium textures, patterns and colours to choose from."),
        ],
        benefits=[
            ("&#129309;", "Seamless Operation", "Smooth cordless and motorized lifts raise and lower with ease."),
            ("&#128118;", "Child-Safe Design", "Cordless construction removes dangerous pull cords."),
            ("&#127807;", "Energy Efficiency", "Optional thermal lining helps insulate against heat and cold."),
            ("&#127912;", "Customizable Styles", "Flat, hobbled and relaxed folds in your choice of fabric."),
            ("&#10024;", "Premium Materials", "Designer textiles and quality hardware built to last."),
            ("&#9881;", "Motorized Option", "Add quiet motorization for one-touch, scheduled control."),
        ],
        specs=[("200+", "Designer fabrics"), ("1-2 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Dining Room"), ("&#128716;", "Bedroom"),
               ("&#127968;", "Home Office"), ("&#127797;", "Sunrooms"), ("&#128701;", "Bathroom"),
               ("&#127970;", "Condos"), ("&#128124;", "Nurseries")],
        faqs=[
            ("What styles of Roman shades do you offer?", "We make flat-fold, hobbled (teardrop) and relaxed Roman shades. Flat folds suit modern rooms, hobbled shades add soft cascading folds, and relaxed Romans give a casual, gentle curve."),
            ("Are Roman shades child-safe?", "Yes. We build them with cordless or motorized lifts by default, eliminating hazardous cords — the safest choice for homes with children and pets."),
            ("Can I add blackout lining to Roman shades?", "Definitely. Blackout and thermal linings are popular for bedrooms and media rooms, adding privacy, light control and insulation."),
            ("How much do Roman shades cost?", "Custom Roman shades generally range from $240 to $420 per window installed depending on fabric and lining. Your free in-home consultation confirms exact pricing."),
        ],
    ),
    "california-shutters": dict(
        name="California Shutters",
        h1=("Custom <em>California Shutters</em> — Built to Add Value"),
        pill="Adds Home Value",
        title="California Shutters GTA | Custom Plantation Shutters — Modern Home Blinds",
        desc="Custom California (plantation) shutters in PVC or real wood, manufactured for the GTA. Adjustable louvres, total privacy and insulation. Free in-home consultation.",
        sub="Solid, framed panels with adjustable louvres that tilt for light and privacy — a permanent, architectural upgrade that buyers love.",
        price=(300, 500),
        ov_title="A permanent upgrade, not just a window covering",
        ov_p=[
            "California shutters (also called plantation shutters) are considered a built-in home improvement. Their wide, adjustable louvres tilt to control light and privacy, while the rigid frame insulates against heat and cold. Unlike soft shades, they add lasting resale value.",
            "Choose durable, moisture-resistant PVC for kitchens and bathrooms, or warm real wood for living spaces and bedrooms. Every shutter is custom-built and professionally installed for a precise, gap-free fit.",
        ],
        bullets=[
            ("PVC or real wood", "Moisture-proof PVC or premium hardwood to match your home."),
            ("Adjustable louvres", "Tilt for the exact light and privacy balance you want."),
            ("Energy efficient", "A rigid, insulating barrier that helps cut heating and cooling costs."),
            ("Boosts resale value", "A timeless, built-in feature that appeals to buyers."),
        ],
        benefits=[
            ("&#128274;", "Total Privacy", "Close the louvres fully for complete privacy, day or night."),
            ("&#127807;", "Insulation", "A solid frame and panels help regulate room temperature year-round."),
            ("&#9776;", "Adjustable Louvres", "Tilt the slats for precise light control and airflow."),
            ("&#128200;", "Adds Home Value", "A premium, permanent fixture that increases resale appeal."),
            ("&#129717;", "PVC or Real Wood", "Choose moisture-proof PVC or warm, natural hardwood."),
            ("&#10024;", "Timeless Style", "Classic, clean lines that suit any era of home."),
        ],
        specs=[("PVC / Wood", "Material options"), ("2-3 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Kitchen"), ("&#128716;", "Bedroom"),
               ("&#128701;", "Bathroom"), ("&#127968;", "Home Office"), ("&#127970;", "Condos"),
               ("&#127797;", "Sunrooms"), ("&#129507;", "Hallways")],
        faqs=[
            ("What is the difference between California and plantation shutters?", "They are the same product. “California shutters” is the common Canadian term for interior plantation shutters with wide, adjustable louvres set in a framed panel."),
            ("Should I choose PVC or wood shutters?", "PVC (vinyl) shutters are moisture- and warp-resistant, making them ideal for kitchens, bathrooms and humid areas. Real wood shutters offer a warmer, premium look for living rooms and bedrooms."),
            ("Do shutters really add home value?", "Yes. Because they are custom-fitted and permanent, California shutters are treated as a built-in upgrade and are a strong selling feature for many GTA buyers."),
            ("How much do California shutters cost?", "Custom shutters typically range from $300 to $500 per window installed depending on material and size. Book a free in-home measurement for an exact quote."),
        ],
    ),
    "silhouette-shades": dict(
        name="Silhouette Shades",
        h1=("Custom <em>Silhouette Shades</em> — Light, Reimagined"),
        pill="Soft Diffused Light",
        title="Silhouette Shades GTA | Sheer Shadings — Modern Home Blinds",
        desc="Custom Silhouette-style sheer shadings manufactured for the GTA. Soft fabric vanes float between sheers for diffused light and UV protection. Free consultation.",
        sub="Soft fabric vanes suspended between two sheers tilt to transform harsh sunlight into a warm, diffused glow — while protecting your floors and furniture from UV.",
        price=(250, 450),
        ov_title="Daylight, beautifully softened",
        ov_p=[
            "Silhouette-style sheer shadings float horizontal fabric vanes between two layers of sheer fabric. Tilt the vanes open to fill the room with soft, diffused daylight and a gentle outward view, or close them for privacy and UV protection — all with no harsh glare.",
            "The effect is luminous and elegant, and the sheers hide the hardware completely for a clean, high-end look. Custom-made and installed for a flawless fit.",
        ],
        bullets=[
            ("Diffused, glare-free light", "Vanes scatter sunlight into a soft, even glow."),
            ("Built-in UV protection", "Helps shield floors, art and furniture from fading."),
            ("Elegant floating vanes", "Hardware hidden between sheers for a refined finish."),
            ("Cordless & child-safe", "Smooth wand or motorized control with no dangling cords."),
        ],
        benefits=[
            ("&#127774;", "Soft Diffused Light", "Vanes transform direct sun into a gentle, even glow."),
            ("&#9925;", "UV Protection", "Filters harmful rays to help protect interiors from fading."),
            ("&#9728;", "Light Control", "Tilt the vanes for anything from full sun to soft privacy."),
            ("&#10024;", "Elegant Look", "A luminous, designer aesthetic that elevates any room."),
            ("&#128118;", "Cordless Option", "Child-safe wand or motorized operation, no cords."),
            ("&#9881;", "Motorized Option", "Add quiet motorization for effortless control."),
        ],
        specs=[("Sheer", "Fabric technology"), ("1-2 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Dining Room"), ("&#128716;", "Bedroom"),
               ("&#127968;", "Home Office"), ("&#127797;", "Sunrooms"), ("&#127970;", "Condos"),
               ("&#129507;", "Foyers"), ("&#128124;", "Nurseries")],
        faqs=[
            ("How do Silhouette sheer shades work?", "Soft fabric vanes are suspended between two sheer fabric panels. Tilting the vanes lets you control light and privacy, while the sheers diffuse incoming sunlight into a soft glow."),
            ("Do sheer shades provide privacy at night?", "With the vanes closed they offer good daytime privacy and a soft silhouette at night. For full nighttime privacy in bedrooms we can pair them with a blackout shade."),
            ("Do these shades block UV rays?", "Yes — the sheer fabric filters a significant amount of UV, helping protect flooring, furniture and artwork from sun fading."),
            ("How much do Silhouette shades cost?", "Sheer shadings typically range from $250 to $450 per window installed depending on size and options. A free in-home consultation confirms your exact price."),
        ],
    ),
    "cellular-shades": dict(
        name="Cellular Shades",
        h1=("Custom <em>Cellular Shades</em> — Insulate & Save"),
        pill="Energy Efficient",
        title="Cellular Shades GTA | Honeycomb Blinds — Modern Home Blinds",
        desc="Custom cellular (honeycomb) shades manufactured for the GTA. Insulating honeycomb cells trap air to save energy. Cordless, child-safe options. Free consultation.",
        sub="Honeycomb-shaped cells trap a layer of air at the window, creating an insulating barrier that keeps rooms warmer in winter, cooler in summer — and lowers your bills.",
        price=(200, 350),
        ov_title="The most energy-efficient shade you can buy",
        ov_p=[
            "Cellular shades — also called honeycomb shades — are engineered with pockets that trap air against the glass. That trapped air is a natural insulator, reducing heat loss in winter and heat gain in summer. For drafty GTA windows, they are the single best shade for comfort and energy savings.",
            "They fold up compactly, come in light-filtering and blackout fabrics, and are available fully cordless for a clean, child-safe finish.",
        ],
        bullets=[
            ("Real energy savings", "Insulating cells reduce heat transfer through your windows."),
            ("Insulating honeycomb", "Single or double-cell construction for extra performance."),
            ("Light-filter or blackout", "Choose the fabric opacity to match each room."),
            ("Cordless & child-safe", "A clean, cord-free look that's safe around kids and pets."),
        ],
        benefits=[
            ("&#127807;", "Energy Efficient", "Trapped air reduces heating and cooling costs year-round."),
            ("&#11041;", "Insulating Honeycomb", "Single or double cells create a thermal barrier at the glass."),
            ("&#9728;", "Light Control", "Light-filtering and blackout fabrics for any room."),
            ("&#128274;", "Privacy", "Closed cells provide excellent privacy day and night."),
            ("&#128118;", "Cordless &amp; Child-Safe", "No cords for a clean, family-friendly finish."),
            ("&#9881;", "Motorized Option", "Add quiet motorization for one-touch control."),
        ],
        specs=[("Up to 2x", "Insulating cell options"), ("1-2 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128716;", "Bedroom"), ("&#128719;", "Living Room"), ("&#127968;", "Home Office"),
               ("&#127970;", "Condos"), ("&#127797;", "Sunrooms"), ("&#128124;", "Nurseries"),
               ("&#127869;", "Kitchen"), ("&#129507;", "Basements")],
        faqs=[
            ("How do cellular shades save energy?", "Their honeycomb cells trap a pocket of air between the room and the window glass. This insulating layer slows heat transfer, keeping rooms warmer in winter and cooler in summer and easing the load on your HVAC."),
            ("What is the difference between single and double cell?", "Single-cell shades have one row of pockets; double-cell shades have two, trapping more air for greater insulation. Double-cell is ideal for very cold or sun-exposed windows."),
            ("Are cellular shades available in blackout?", "Yes. Blackout (room-darkening) honeycomb fabrics are popular for bedrooms and nurseries, combining insulation with near-total light blocking."),
            ("How much do cellular shades cost?", "Cellular shades typically range from $200 to $350 per window installed depending on cell type and fabric. Book a free measurement for an exact quote."),
        ],
    ),
    "draperies-sheers": dict(
        name="Draperies & Sheers",
        h1=("Custom <em>Draperies &amp; Sheers</em> — Hand-Sewn Luxury"),
        pill="Luxury Finish",
        title="Custom Draperies & Sheers GTA | Drapes & Curtains — Modern Home Blinds",
        desc="Custom hand-sewn draperies and sheers, made to your exact dimensions in Oakville. Floor-to-ceiling luxury, fully customizable. Free GTA consultation.",
        sub="Floor-to-ceiling fabric, fully lined and hand-sewn to your exact dimensions — the finishing touch that makes a room feel complete.",
        price=(350, 600),
        ov_title="The statement layer that ties a room together",
        ov_p=[
            "Nothing softens and elevates a space like custom draperies. Hung floor-to-ceiling and tailored to your windows, they add height, warmth and a sense of luxury that ready-made panels can't match. Pair heavier drapery with airy sheers for a layered look that controls light beautifully at any time of day.",
            "We measure, sew and hang every panel ourselves — choosing the right fullness, heading style, lining and hardware so the finished result drapes perfectly.",
        ],
        bullets=[
            ("Hand-sewn to measure", "Tailored to your exact window height and width."),
            ("Floor-to-ceiling drama", "Mounted high and wide to make rooms feel larger."),
            ("Fully customizable", "Hundreds of fabrics, headings, linings and hardware finishes."),
            ("Layer with sheers", "Combine drapery and sheers for day-to-night light control."),
        ],
        benefits=[
            ("&#10024;", "Luxury Finish", "Rich, tailored fabric that instantly elevates a room."),
            ("&#128207;", "Floor-to-Ceiling", "Full-height panels that add drama and a sense of space."),
            ("&#129526;", "Hand-Sewn", "Crafted to your exact measurements for a flawless drape."),
            ("&#127912;", "Fully Customizable", "Choose fabric, heading style, lining and hardware."),
            ("&#127774;", "Light Filtering", "Layer sheers and drapes to control light all day."),
            ("&#9881;", "Motorized Option", "Add a quiet motorized track for one-touch operation."),
        ],
        specs=[("300+", "Designer fabrics"), ("2-3 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Dining Room"), ("&#128716;", "Bedroom"),
               ("&#127968;", "Home Office"), ("&#127970;", "Condos"), ("&#127797;", "Sunrooms"),
               ("&#129507;", "Foyers"), ("&#128124;", "Nurseries")],
        faqs=[
            ("Can I pair draperies with blinds or shades?", "Yes — layering is one of our most requested looks. Functional blinds or shades handle privacy and light control, while drapery adds softness, colour and a finished, designer feel."),
            ("What is the difference between drapes and sheers?", "Drapes are heavier, often lined panels that provide privacy and insulation. Sheers are lightweight and translucent, filtering light softly while keeping a bright, airy feel. Many clients use both together."),
            ("Can draperies be motorized?", "Yes. We install quiet motorized drapery tracks that open and close with a remote, app, schedule or voice command — ideal for tall or wide windows."),
            ("How much do custom draperies cost?", "Custom draperies typically range from $350 to $600 per window installed depending on fabric, fullness and lining. Your free consultation provides an exact quote."),
        ],
    ),
    "motorized-blinds": dict(
        name="Motorized & Smart Blinds",
        h1=("<em>Motorized &amp; Smart</em> Blinds"),
        pill="Smart Home Ready",
        title="Motorized Blinds GTA | Smart Shades — Modern Home Blinds",
        desc="Motorized and smart blinds for the GTA. App, remote and voice control with scheduling. Perfect for high windows. Free in-home consultation.",
        sub="Open and close your shades with a tap, a voice command, or on an automatic schedule. Whisper-quiet motors bring effortless control to every window — even the ones you can't reach.",
        price=None,
        price_note="Motorization adds roughly $200 per window over manual pricing.",
        ov_title="Your windows, fully automated",
        ov_p=[
            "Motorized blinds remove the cords and the effort. With reliable motors you can raise and lower shades from a remote, your phone, or a simple voice command to Alexa, Google Home or Apple HomeKit. Set schedules so blinds wake with the sun and close at dusk — saving energy and adding security while you're away.",
            "Almost any of our products can be motorized: zebra blinds, roller and solar shades, Romans, cellular shades, sheers and drapery tracks. We handle the wiring or recharge-battery setup and program everything for you.",
        ],
        bullets=[
            ("App & voice control", "Control from your phone or with Alexa, Google &amp; HomeKit."),
            ("Set-and-forget schedules", "Automate open and close times for comfort and energy savings."),
            ("Perfect for high windows", "Operate tall, wide or hard-to-reach windows effortlessly."),
            ("Cord-free & child-safe", "No cords means a cleaner look and a safer home."),
        ],
        benefits=[
            ("&#128241;", "App &amp; Voice Control", "Operate from your phone or with Alexa, Google Home and HomeKit."),
            ("&#9889;", "Motor Powered", "Reliable, whisper-quiet motors from the global leader."),
            ("&#9201;", "Schedule Automation", "Open and close automatically around your daily routine."),
            ("&#128205;", "Great for High Windows", "Effortless control of tall and hard-to-reach openings."),
            ("&#127807;", "Energy Saving", "Automate shades to reduce heating and cooling loads."),
            ("&#128274;", "Added Security", "Scheduled movement makes your home look lived-in."),
        ],
        specs=[("Smart", "Motor technology"), ("Battery / Wired", "Power options"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#128716;", "Bedroom"), ("&#127968;", "Home Office"),
               ("&#127970;", "Condos"), ("&#127797;", "Sunrooms"), ("&#128205;", "High Windows"),
               ("&#127902;", "Media Room"), ("&#127869;", "Kitchen")],
        faqs=[
            ("Which blinds can be motorized?", "Almost all of them — zebra blinds, roller and solar shades, Roman shades, cellular shades, sheers and even drapery tracks can be motorized with smart motors."),
            ("Do motorized blinds need to be hardwired?", "Not necessarily. Most of our motors are rechargeable-battery powered, so no electrician is required. Hardwired options are available for new builds or permanent installations."),
            ("Can I control them with my voice or phone?", "Yes. With a smart hub you can control shades from a smartphone app and through Alexa, Google Home and Apple HomeKit, plus set automatic schedules and scenes."),
            ("How much does motorization cost?", "Motorization typically adds about $200 per window on top of the manual price of your chosen shade. Your free consultation provides exact, all-in pricing."),
        ],
    ),
    "soft-vertical-blinds": dict(
        name="Soft Vertical Blinds",
        h1=("Custom <em>Soft Vertical Blinds</em> for Wide Windows"),
        pill="Patio Door Ready",
        title="Soft Vertical Blinds GTA | Patio Door Shades — Modern Home Blinds",
        desc="Custom soft vertical blinds for sliding doors and wide windows across the GTA. Sleek fabric vanes, no size restrictions, easy glare control. Free consultation.",
        sub="Soft fabric vertical vanes glide smoothly across sliding doors and expansive windows — combining the easy operation of a vertical blind with the elegance of a fabric shade.",
        price=(140, 240),
        ov_title="Built for sliding doors and big windows",
        ov_p=[
            "Soft vertical blinds replace the old, rattly plastic vanes with smooth, fabric-wrapped verticals that stack neatly to one side. They are the ideal solution for patio doors and wide windows, where they manage glare and privacy without taking up floor space.",
            "Rotate the vanes to control light and view, or draw them fully aside for clear access to your door. Available in a wide range of fabrics to coordinate with the rest of your window coverings.",
        ],
        bullets=[
            ("Made for patio doors", "Slide aside cleanly for easy access to sliding doors."),
            ("No size restrictions", "Cover very wide or tall openings other shades can't."),
            ("Space-saving design", "Vanes stack to the side rather than into your room."),
            ("Simple glare control", "Rotate the vanes to dial in light, view and privacy."),
        ],
        benefits=[
            ("&#129519;", "Sleek &amp; Space-Saving", "Slim fabric vanes stack neatly to the side."),
            ("&#128682;", "Patio Door Ready", "Glides aside for easy access to sliding doors."),
            ("&#128208;", "No Size Restrictions", "Spans very wide and tall windows with ease."),
            ("&#127774;", "Manage Glare", "Rotate the vanes to control sun and reflections."),
            ("&#128077;", "Easy Operation", "Smooth wand or cord control for daily use."),
            ("&#9881;", "Motorized Option", "Add quiet motorization for one-touch control."),
        ],
        specs=[("Any size", "Wide-window ready"), ("1-2 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128682;", "Patio Doors"), ("&#128719;", "Living Room"), ("&#127869;", "Dining Room"),
               ("&#127968;", "Home Office"), ("&#127970;", "Condos"), ("&#127797;", "Sunrooms"),
               ("&#128716;", "Bedroom"), ("&#129507;", "Basements")],
        faqs=[
            ("Are soft vertical blinds good for patio doors?", "Yes — they are one of the best options for sliding patio doors. The vanes draw cleanly to one side for full access and rotate to control light and privacy without intruding into the room."),
            ("How are soft verticals different from old vertical blinds?", "Instead of stiff plastic louvres, soft verticals use fabric-wrapped vanes that look and feel like a soft shade. They are quieter, more elegant and far less prone to clattering."),
            ("Can vertical blinds cover very large windows?", "Absolutely. Vertical blinds have essentially no width limit, making them ideal for floor-to-ceiling windows and wide openings other shades struggle to cover."),
            ("How much do soft vertical blinds cost?", "Soft vertical blinds typically range from $140 to $240 per window installed depending on size and fabric. Book a free measurement for an exact quote."),
        ],
    ),
    "wood-california-shutters": dict(
        name="Wood California Shutters",
        h1=("Real <em>Wood California Shutters</em>"),
        pill="Premium Hardwood",
        title="Wood California Shutters GTA | Real Wood Plantation Shutters — Modern Home Blinds",
        desc="Real wood California (plantation) shutters, custom built for the GTA. Warm natural hardwood, adjustable louvres, lasting value. Free in-home consultation.",
        sub="Genuine hardwood plantation shutters with the warmth, weight and timeless grain that only real wood delivers — a true built-in upgrade for your home.",
        price=(350, 550),
        ov_title="The richness of natural wood",
        ov_p=[
            "Real wood California shutters are crafted from premium kiln-dried hardwood, prized for their warmth, fine grain and substantial feel. Wide adjustable louvres tilt to control light and privacy, while the solid framed panels add insulation and a permanent, architectural presence to any room.",
            "Wood is the choice for living rooms, dining rooms and bedrooms where appearance matters most. Each shutter is custom-built and professionally installed for a flawless, gap-free fit.",
        ],
        bullets=[
            ("Premium hardwood", "Lightweight, kiln-dried wood with a fine, paintable grain."),
            ("Adjustable louvres", "Tilt for precise light, view and privacy control."),
            ("Stain or paint finishes", "Match your trim, floors or cabinetry."),
            ("Adds lasting value", "A permanent, built-in feature buyers love."),
        ],
        benefits=[
            ("&#129717;", "Real Hardwood", "Warm, premium wood with a beautiful natural grain."),
            ("&#9776;", "Adjustable Louvres", "Tilt the slats for full control of light and airflow."),
            ("&#127802;", "Custom Finishes", "Choose from a range of stains and painted colours."),
            ("&#127807;", "Insulation", "Solid panels help regulate room temperature year-round."),
            ("&#128200;", "Adds Home Value", "A timeless, built-in upgrade with strong resale appeal."),
            ("&#9728;", "Total Privacy", "Close the louvres fully for complete privacy."),
        ],
        specs=[("Hardwood", "Premium material"), ("2-3 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Dining Room"), ("&#128716;", "Bedroom"),
               ("&#127968;", "Home Office"), ("&#129507;", "Foyers"), ("&#127970;", "Condos"),
               ("&#127797;", "Sunrooms"), ("&#129507;", "Hallways")],
        faqs=[
            ("Why choose real wood over vinyl shutters?", "Real wood offers a warmer, richer look with a natural grain and a more substantial feel. It is lighter than vinyl over wide spans and takes stain or paint beautifully — ideal for living areas and bedrooms where appearance is the priority."),
            ("Are wood shutters suitable for bathrooms?", "For high-humidity rooms like bathrooms and kitchens we usually recommend vinyl (PVC) shutters, which resist moisture and warping. Wood is best for dry living spaces."),
            ("Can wood shutters be stained to match my floors?", "Yes. We offer a wide range of stains and painted finishes so your shutters can complement your trim, flooring or cabinetry."),
            ("How much do wood California shutters cost?", "Real wood shutters typically range from $350 to $550 per window installed depending on size and finish. Book a free in-home measurement for an exact quote."),
        ],
    ),
    "vinyl-california-shutters": dict(
        name="Vinyl California Shutters",
        h1=("Durable <em>Vinyl California Shutters</em>"),
        pill="Moisture-Proof",
        title="Vinyl California Shutters GTA | PVC Plantation Shutters — Modern Home Blinds",
        desc="Vinyl (PVC) California shutters custom built for the GTA. Moisture-proof, warp-resistant, easy to clean. Ideal for kitchens and bathrooms. Free consultation.",
        sub="Maintenance-free PVC plantation shutters that won't warp, crack or fade — engineered for kitchens, bathrooms and any room where durability matters most.",
        price=(300, 450),
        ov_title="All the style, none of the upkeep",
        ov_p=[
            "Vinyl (PVC) California shutters give you the classic plantation-shutter look with unbeatable durability. Because they are moisture- and warp-resistant, they thrive in humid spaces like kitchens, bathrooms and laundry rooms where wood can't. A quick wipe keeps them looking new for years.",
            "Wide adjustable louvres tilt for light and privacy, and the rigid frame adds insulation. Custom-built and professionally installed for a precise, gap-free fit.",
        ],
        bullets=[
            ("Moisture-proof PVC", "Won't warp, crack, peel or fade in humid rooms."),
            ("Wipe-clean finish", "Maintenance-free — just wipe with a damp cloth."),
            ("Adjustable louvres", "Tilt for the exact light and privacy you want."),
            ("Great value", "Premium shutter looks at a friendlier price than wood."),
        ],
        benefits=[
            ("&#128166;", "Moisture-Proof", "Ideal for bathrooms, kitchens and humid areas."),
            ("&#129529;", "Easy To Clean", "Wipe-clean PVC that always looks fresh."),
            ("&#9776;", "Adjustable Louvres", "Precise control of light, view and airflow."),
            ("&#127807;", "Insulation", "Solid panels help keep rooms comfortable year-round."),
            ("&#128176;", "Great Value", "Classic shutter style at an accessible price."),
            ("&#128200;", "Adds Home Value", "A permanent, built-in upgrade buyers appreciate."),
        ],
        specs=[("PVC", "Moisture-proof material"), ("2-3 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#127869;", "Kitchen"), ("&#128701;", "Bathroom"), ("&#129532;", "Laundry"),
               ("&#128716;", "Bedroom"), ("&#128719;", "Living Room"), ("&#127970;", "Condos"),
               ("&#127797;", "Sunrooms"), ("&#129507;", "Basements")],
        faqs=[
            ("Are vinyl shutters as good as wood?", "Vinyl shutters share the same classic plantation look and adjustable-louvre function. They are more durable in humidity and lower maintenance than wood, though wood offers a warmer grain for living spaces. Many homes use vinyl in wet rooms and wood elsewhere."),
            ("Will vinyl shutters yellow or fade over time?", "Quality PVC shutters are UV-stabilised to resist yellowing and fading, so they stay looking clean and white for years even in sunny windows."),
            ("Are vinyl shutters good for bathrooms?", "Yes — they are the ideal choice. PVC is completely moisture-resistant, so it won't warp or crack in bathrooms, kitchens or laundry rooms."),
            ("How much do vinyl California shutters cost?", "Vinyl shutters typically range from $300 to $450 per window installed depending on size. Book a free in-home measurement for your exact price."),
        ],
    ),
    "faux-wood-blinds": dict(
        name="Faux Wood Blinds",
        h1=("Custom <em>Faux Wood Blinds</em> — Wood Look, Worry-Free"),
        pill="Moisture-Resistant",
        title="Faux Wood Blinds GTA | Composite Horizontal Blinds — Modern Home Blinds",
        desc="Custom faux wood blinds for the GTA. The warm look of real wood with moisture resistance and easy care. Perfect for kitchens and baths. Free consultation.",
        sub="Wide horizontal slats with the warm appearance of real wood, made from durable composite that resists humidity, warping and fading — for a fraction of the cost.",
        price=(150, 250),
        ov_title="The look of wood, built for real life",
        ov_p=[
            "Faux wood blinds give you the classic, timeless look of wood-slat blinds without the worry. Made from a tough composite, they shrug off humidity, sunlight and daily wear, so they stay straight and true in kitchens, bathrooms and sunny windows where real wood can warp.",
            "Tilt the slats for light and privacy, or raise them out of the way entirely. Available in a range of wood-tone and painted finishes to suit any room — at a budget-friendly price.",
        ],
        bullets=[
            ("Real wood appearance", "Warm wood-grain looks in a durable composite slat."),
            ("Humidity resistant", "Won't warp or crack in kitchens and bathrooms."),
            ("Easy to clean", "Just dust or wipe the slats — no special care needed."),
            ("Budget friendly", "A premium look at an accessible price point."),
        ],
        benefits=[
            ("&#129717;", "Wood-Look Finish", "The warm character of wood in tough composite slats."),
            ("&#128166;", "Moisture-Resistant", "Stays straight and true in humid rooms."),
            ("&#9776;", "Tilt Light Control", "Angle the slats for precise light and privacy."),
            ("&#129529;", "Easy To Clean", "Wipe or dust — no fading, warping or fuss."),
            ("&#128176;", "Great Value", "Designer wood looks at a friendly price."),
            ("&#127912;", "Many Finishes", "Wood tones and painted colours to match any decor."),
        ],
        specs=[("2\"-2.5\"", "Slat width options"), ("1-2 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#127869;", "Kitchen"), ("&#128701;", "Bathroom"), ("&#128716;", "Bedroom"),
               ("&#128719;", "Living Room"), ("&#127968;", "Home Office"), ("&#129532;", "Laundry"),
               ("&#127970;", "Condos"), ("&#129507;", "Basements")],
        faqs=[
            ("What is the difference between faux wood and real wood blinds?", "Faux wood blinds are made from a composite material that mimics wood grain but resists moisture and warping. Real wood blinds are lighter and offer a genuine grain, but can warp in humidity. Faux wood is the practical, value choice for most rooms."),
            ("Are faux wood blinds good for bathrooms and kitchens?", "Yes — they are an excellent choice. Because the composite slats resist humidity and heat, they stay straight and look great in bathrooms, kitchens and laundry rooms."),
            ("Do faux wood blinds look like real wood?", "Modern faux wood blinds feature realistic wood-grain textures and finishes that closely resemble real wood, often indistinguishable from a short distance."),
            ("How much do faux wood blinds cost?", "Faux wood blinds typically range from $150 to $250 per window installed depending on size and finish. Book a free measurement for an exact quote."),
        ],
    ),
    "outdoor-patio-awnings": dict(
        name="Outdoor Patio Awnings",
        h1=("Custom <em>Outdoor Patio Awnings</em> & Shades"),
        pill="Beat The Heat",
        title="Outdoor Patio Awnings GTA | Retractable Awnings & Sun Shades — Modern Home Blinds",
        desc="Custom outdoor patio awnings and retractable shades for the GTA. Block sun and heat, extend your outdoor season. Motorized options. Free consultation.",
        sub="Extend your living space outdoors. Retractable awnings and exterior shades block sun and heat on demand, keeping patios, decks and windows cool and comfortable.",
        price=None,
        price_note="Outdoor awnings are quoted per project after a free site visit.",
        ov_title="Shade where you need it most — outside",
        ov_p=[
            "Outdoor awnings and patio shades let you reclaim your deck, patio or balcony from the summer sun. Roll them out to create cool, shaded comfort for entertaining, then retract them to enjoy open sky. They also shade sun-facing windows, dramatically reducing indoor heat gain and cooling costs.",
            "Choose durable, fade- and weather-resistant outdoor fabrics, with manual or motorized operation — including wind and sun sensors that retract the awning automatically to protect it.",
        ],
        bullets=[
            ("Block sun &amp; heat", "Keep patios and rooms cooler all summer long."),
            ("Retractable on demand", "Extend for shade, retract for open sky."),
            ("Weatherproof fabrics", "UV- and fade-resistant materials built for the outdoors."),
            ("Motorized &amp; sensors", "Optional remote, sun and wind sensors for hands-free use."),
        ],
        benefits=[
            ("&#9925;", "Sun &amp; Heat Block", "Dramatically reduce heat on patios and through windows."),
            ("&#128259;", "Retractable", "Roll out for shade and retract when you want sky."),
            ("&#127786;", "Weather-Resistant", "Tough outdoor fabrics resist UV, fading and the elements."),
            ("&#9881;", "Motorized Option", "Add remote control plus sun and wind sensors."),
            ("&#127777;", "Cooler Interiors", "Exterior shade cuts cooling costs better than blinds alone."),
            ("&#127968;", "Expand Your Space", "Make decks and balconies usable all season."),
        ],
        specs=[("Outdoor", "Weatherproof fabrics"), ("By project", "Custom quoted"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "On-site consultation")],
        rooms=[("&#127777;", "Patios"), ("&#128694;", "Decks"), ("&#127970;", "Balconies"),
               ("&#127869;", "Outdoor Dining"), ("&#127968;", "Porches"), ("&#9728;", "Sun-Facing Windows"),
               ("&#127881;", "Entertaining"), ("&#127798;", "Gardens")],
        faqs=[
            ("Are outdoor awnings retractable?", "Yes. Our retractable awnings extend to provide shade and roll back neatly when not needed, so you control sun and sky on demand. Fixed and motorized versions are available."),
            ("Can awnings be motorized?", "Absolutely. Motorized awnings operate with a remote or wall switch, and can include sun and wind sensors that automatically extend for shade or retract to protect the awning in high winds."),
            ("Do patio awnings help reduce cooling costs?", "Yes — significantly. Blocking sunlight outside the glass stops heat before it enters, making exterior shade far more effective at reducing cooling costs than interior blinds alone."),
            ("How are outdoor awnings priced?", "Because sizes and mounting vary widely, awnings are quoted per project after a free on-site consultation. We assess your space and provide a clear, all-in estimate."),
        ],
    ),
    "skylight-cellular-blinds": dict(
        name="Skylight Cellular Blinds",
        h1=("Custom <em>Skylight Cellular Blinds</em>"),
        pill="For Overhead Windows",
        title="Skylight Cellular Blinds GTA | Skylight Shades — Modern Home Blinds",
        desc="Custom skylight cellular (honeycomb) blinds for the GTA. Insulate overhead windows, control light and glare, reduce energy loss. Free consultation.",
        sub="Honeycomb shades engineered for overhead and angled skylight windows — taming glare and heat while insulating the hardest-working windows in your home.",
        price=(280, 480),
        ov_title="Finally, control over your skylights",
        ov_p=[
            "Skylights flood a home with daylight, but they also leak heat in winter, magnify summer warmth and create glare. Skylight cellular blinds solve all three. Their insulating honeycomb cells trap air against the glass, while a specialised track system holds the shade flat against angled or overhead windows.",
            "Operate them with an extension pole or — far more popular for hard-to-reach skylights — a quiet motor with remote and scheduling. Made to measure for a precise fit.",
        ],
        bullets=[
            ("Built for skylights", "Track system keeps shades flat on angled or overhead glass."),
            ("Insulating honeycomb", "Cuts the heat loss and gain skylights are notorious for."),
            ("Tame glare", "Soften harsh overhead sun and protect floors from fading."),
            ("Motor-ready", "Quiet motorization is ideal for out-of-reach skylights."),
        ],
        benefits=[
            ("&#128205;", "Skylight-Specific", "Engineered to sit flat on overhead and sloped windows."),
            ("&#127807;", "Energy Efficient", "Honeycomb cells stop heat escaping through skylights."),
            ("&#9925;", "Glare &amp; UV Control", "Soften harsh overhead light and protect interiors."),
            ("&#9881;", "Motorized Option", "Remote and scheduled control for hard-to-reach windows."),
            ("&#9728;", "Light Control", "Light-filtering and blackout fabrics available."),
            ("&#128274;", "Privacy", "Closed cells provide privacy and a clean finish."),
        ],
        specs=[("Angled fit", "Skylight track system"), ("2-3 wk", "Typical lead time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128716;", "Bedroom"), ("&#128719;", "Living Room"), ("&#127869;", "Kitchen"),
               ("&#128701;", "Bathroom"), ("&#127968;", "Home Office"), ("&#127797;", "Sunrooms"),
               ("&#129507;", "Stairwells"), ("&#127970;", "Lofts")],
        faqs=[
            ("Can blinds be fitted to skylight windows?", "Yes. Skylight cellular blinds use a side-track system that holds the honeycomb shade flat against angled, sloped or overhead glass so it stays in place at any position."),
            ("Do skylight blinds help with heat and energy loss?", "Very much so. Skylights are a major source of heat loss and gain. The insulating honeycomb cells trap air at the glass, helping keep rooms comfortable and lowering energy bills."),
            ("How do I operate a skylight blind I can't reach?", "Most clients choose motorization with a remote and schedules. A manual extension pole is also available for skylights within reach."),
            ("How much do skylight cellular blinds cost?", "Skylight cellular blinds typically range from $280 to $480 per window installed depending on size and operation. Book a free measurement for an exact quote."),
        ],
    ),
    "smart-film": dict(
        name="Smart Film",
        h1=("<em>Smart Film</em> — Switchable Privacy Glass"),
        pill="Switchable Glass",
        title="Smart Film GTA | Switchable Privacy Glass Film — Modern Home Blinds",
        desc="Switchable smart film for the GTA — turn glass from clear to frosted at the touch of a button. Instant privacy for offices, condos and homes. Free consultation.",
        sub="Switch any glass from crystal clear to opaque frosted in an instant. Smart film delivers on-demand privacy with no blinds, no curtains — just a tap.",
        price=None,
        price_note="Smart film is quoted per project after a free site assessment.",
        ov_title="Privacy at the touch of a button",
        ov_p=[
            "Smart film (PDLC switchable film) is applied to glass and wired to power. Switch it on and the glass is perfectly clear; switch it off and it turns instantly to a private frosted finish. It is a sleek, modern alternative to blinds for glass partitions, doors, condos and offices — and doubles as a projection surface when frosted.",
            "Ideal where a clean, minimal look is essential and where traditional window coverings won't work. We assess your glass, supply and install, and handle the electrical connection.",
        ],
        bullets=[
            ("Clear-to-frosted instantly", "Switch privacy on and off at the touch of a button."),
            ("No blinds needed", "A minimal, modern look with nothing hanging over the glass."),
            ("Great for partitions", "Perfect for office glass walls, doors and condo windows."),
            ("Projection ready", "The frosted state doubles as a projection screen."),
        ],
        benefits=[
            ("&#9889;", "Instant Privacy", "Switch glass from clear to frosted in milliseconds."),
            ("&#128241;", "Smart Control", "Operate by switch, remote, app or automation."),
            ("&#10024;", "Minimal &amp; Modern", "A clean look with no blinds or curtains."),
            ("&#127909;", "Projection Surface", "Use the frosted state as a built-in screen."),
            ("&#9925;", "UV Reduction", "Helps block UV to protect interiors."),
            ("&#127970;", "Office &amp; Condo Ready", "Ideal for glass partitions, doors and high-rises."),
        ],
        specs=[("Clear&#8596;Frosted", "Switchable glass"), ("By project", "Custom quoted"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "On-site consultation")],
        rooms=[("&#127970;", "Offices"), ("&#129695;", "Glass Partitions"), ("&#128682;", "Glass Doors"),
               ("&#127968;", "Condos"), ("&#128701;", "Bathrooms"), ("&#127973;", "Meeting Rooms"),
               ("&#127909;", "Media Rooms"), ("&#127978;", "Storefronts")],
        faqs=[
            ("What is smart film?", "Smart film is a switchable PDLC layer applied to glass and connected to power. When energised the glass is clear; when off it turns to a private frosted state. It gives instant, on-demand privacy without blinds or curtains."),
            ("Where is smart film typically used?", "It is popular for office glass partitions and doors, meeting rooms, condo windows, bathrooms and any space where a clean, modern look and switchable privacy are desired."),
            ("Can smart film be controlled remotely?", "Yes. Beyond a simple wall switch, smart film can be controlled by remote, smartphone app or integrated into home and building automation systems."),
            ("How is smart film priced?", "Because every glass surface and electrical setup is different, smart film is quoted per project after a free on-site assessment, with a clear all-in estimate."),
        ],
    ),
}


def nav_dropdown(active_slug):
    items = []
    for slug, name in CATALOG:
        cls = ' class="active"' if slug == active_slug else ""
        items.append(f'          <a href="{slug}.html"{cls}>{name}</a>')
    return "\n".join(items)


def footer_products():
    rows = []
    for slug, name in CATALOG[:7]:
        rows.append(f'        <li><a href="{slug}.html">{name}</a></li>')
    return "\n".join(rows)


def related_cards(active_slug):
    # pick the first three products that aren't the current one
    rel = [(s, n) for s, n in CATALOG if s != active_slug][:3]
    cards = []
    for slug, name in rel:
        img = IMG[slug]
        cards.append(f'''      <div class="rel-card" onclick="location='{slug}.html'">
        <img src="assets/{img}" alt="{name}" loading="lazy"/>
        <div class="body"><h3>{name}</h3><div class="link">View Product &#8594;</div></div>
      </div>''')
    return "\n".join(cards)


def render(slug, p):
    img = IMG[slug]
    name = p["name"]
    # price block
    if p.get("price"):
        lo, hi = p["price"]
        price_block = f'''        <div class="price-tag">
          <span class="from">From</span>
          <span class="amt">${lo}<small> &ndash; ${hi} / window installed</small></span>
        </div>'''
    else:
        note = p.get("price_note", "")
        price_block = f'''        <div class="price-tag">
          <span class="from">Smart Upgrade</span>
          <span class="amt">+$200<small> / window approx.</small></span>
        </div>'''

    bullets = "\n".join(
        f'        <li><span><strong>{b[0]}.</strong> {b[1]}</span></li>' for b in p["bullets"]
    )
    benefits = "\n".join(
        f'''      <div class="ben-card">
        <div class="ben-icon">{ic}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>''' for ic, t, d in p["benefits"]
    )
    specs = "\n".join(
        f'      <div class="spec-item"><div class="num">{n}</div><div class="lbl">{l}</div></div>'
        for n, l in p["specs"]
    )
    rooms = "\n".join(
        f'      <div class="room-chip"><span>{e}</span>{r}</div>' for e, r in p["rooms"]
    )
    faqs = "\n".join(
        f'''      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">{q}<span class="faq-arrow">&#9662;</span></button>
        <div class="faq-a"><p>{a}</p></div>
      </div>''' for q, a in p["faqs"]
    )

    # JSON-LD FAQ schema
    faq_ld = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (json_str(q), json_str(strip_tags(a))) for q, a in p["faqs"]
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}"/>
<meta property="og:title" content="{name} | Modern Home Blinds"/>
<meta property="og:description" content="{p["desc"]}"/>
<meta property="og:type" content="product"/>
<meta property="og:url" content="https://www.modernhomeblinds.ca/{slug}.html"/>
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
<link rel="canonical" href="https://www.modernhomeblinds.ca/{slug}.html"/>
<meta property="og:site_name" content="Modern Home Blinds"/>
<meta property="og:locale" content="en_CA"/>
<meta property="og:image" content="https://www.modernhomeblinds.ca/assets/og-image.jpg"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="https://www.modernhomeblinds.ca/assets/og-image.jpg"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="icon" href="/assets/logo.png" sizes="any"/>
<link rel="apple-touch-icon" href="/assets/logo.png"/>
<link rel="manifest" href="/site.webmanifest"/>
<meta name="theme-color" content="#0f0f0f"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500;1,9..144,600&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="assets/product.css"/>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_ld}]}}
</script>
<!-- Nextdoor Pixel Code -->
<script type='text/javascript'>
  !function(e,n){{var t,p;e.ndp||((t=e.ndp=function(){{
  t.handleRequest?t.handleRequest.apply(t,arguments):t.queue.push(arguments)
  }}).queue=[],t.v=1,(p=n.createElement(e="script")).async=!0,
  p.src="https://ads.nextdoor.com/public/pixel/ndp.js?id=8154d6e0-e333-4b35-bb55-59eae1b53157",
  (n=n.getElementsByTagName(e)[0]).parentNode.insertBefore(p,n))
  }}(window,document);

  ndp('init','8154d6e0-e333-4b35-bb55-59eae1b53157', {{}});
  ndp('track','PAGE_VIEW');
</script>
<noscript>
  <img height="1" width="1" style="display:none"
     src="https://flask.nextdoor.com/pixel?pid=8154d6e0-e333-4b35-bb55-59eae1b53157&ev=PAGE_VIEW&noscript=1"/>
</noscript>
<!-- End Nextdoor Pixel Code -->
</head>
<body>

<!-- ANNOUNCEMENT BAR -->
<div class="ann">Free In-Home Consultation <b>&middot;</b> Manufactured in Oakville <b>&middot;</b> Installed in Under 1 Week</div>

<!-- NAV -->
<nav class="nav" id="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo"><img src="assets/logo.png" alt="Modern Home Blinds"/></a>
    <ul class="nav-links" id="navLinks">
      <li><a href="index.html">Home</a></li>
      <li class="has-drop"><a href="#">Products &#9662;</a>
        <div class="dropdown">
{nav_dropdown(slug)}
        </div>
      </li>
      <li><a href="index.html#about">About</a></li>
      <li><a href="index.html#estimate">Get Estimate</a></li>
      <li><a href="index.html#compare">Why Us</a></li>
      <li><a href="index.html#faq">FAQ</a></li>
      <li><a href="index.html#contact">Contact</a></li>
    </ul>
    <div class="nav-right">
      <a href="tel:{PHONE_TEL}" class="nav-phone">{PHONE}</a>
      <a href="index.html#consult" class="nav-cta">Free Consultation</a>
      <button class="hamburger" onclick="toggleNav()" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

<!-- BREADCRUMB -->
<div class="crumb">
  <div class="crumb-inner"><a href="index.html">Home</a> &nbsp;/&nbsp; <a href="index.html#products">Products</a> &nbsp;/&nbsp; <span>{name}</span></div>
</div>

<!-- HERO -->
<header class="phero">
  <div class="phero-bg"><img src="assets/{img}" alt="{name} in a GTA home"/></div>
  <div class="phero-overlay"></div>
  <div class="phero-inner">
    <div class="pill">{p["pill"]}</div>
    <h1>{p["h1"]}</h1>
    <p class="phero-sub">{p["sub"]}</p>
    <div class="phero-cta">
      <a href="index.html#consult" class="btn btn-gold">Book Free Consultation &#8594;</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">Call {PHONE}</a>
    </div>
    <div class="phero-trust">
      <span class="phero-star">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
      <span class="phero-trust-txt"><strong>5.0</strong> on Google &middot; <strong>10,000+</strong> windows dressed across the GTA</span>
    </div>
  </div>
</header>

<!-- OVERVIEW -->
<section>
  <div class="inner">
    <div class="split">
      <div>
        <div class="s-label">{name}</div>
        <h2 class="s-title">{p["ov_title"]}</h2>
        {''.join(f'<p class="s-body" style="margin-bottom:14px">{para}</p>' for para in p["ov_p"])}
        <ul class="bullets">
{bullets}
        </ul>
      </div>
      <div class="split-img-wrap">
        <img src="assets/{img}" alt="Custom {name} by Modern Home Blinds"/>
      </div>
    </div>
  </div>
</section>

<!-- BENEFITS -->
<section class="ben-section">
  <div class="inner">
    <div class="center">
      <div class="s-label">Why Homeowners Love Them</div>
      <h2 class="s-title">Key Benefits of {name}</h2>
      <p class="s-body" style="margin:0 auto">Everything you get when you choose custom {name.lower()} from our local Oakville team.</p>
    </div>
    <div class="ben-grid">
{benefits}
    </div>
  </div>
</section>

<!-- SPECS STRIP -->
<section style="padding-top:64px;padding-bottom:64px">
  <div class="inner center">
    <div class="s-label">At A Glance</div>
    <h2 class="s-title">Custom-Made, Locally Installed</h2>
    <div class="spec-grid">
{specs}
    </div>
  </div>
</section>

<!-- ROOMS -->
<section style="background:var(--white);padding-top:64px">
  <div class="inner center">
    <div class="s-label">Where They Work Best</div>
    <h2 class="s-title">Perfect For Rooms Like These</h2>
    <p class="s-body" style="margin:0 auto">Not sure where {name.lower()} fit? Our designers help you choose the right product for every room during your free consultation.</p>
    <div class="room-grid">
{rooms}
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="faq-section">
  <div class="inner">
    <div class="center">
      <div class="s-label">Good To Know</div>
      <h2 class="s-title">{name} FAQ</h2>
    </div>
    <div class="faq-wrap">
{faqs}
    </div>
  </div>
</section>

<!-- CTA BAND -->
<section class="cta-band">
  <div class="inner">
    <h2>Ready for custom {name.lower()}?</h2>
    <p>Book your free, no-obligation in-home consultation. We measure, manufacture in Oakville, and install &mdash; usually within a week.</p>
    <div class="btns">
      <a href="index.html#consult" class="btn btn-gold">Book Free Consultation &#8594;</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">Call {PHONE}</a>
    </div>
  </div>
</section>

<!-- RELATED -->
<section>
  <div class="inner">
    <div class="center">
      <div class="s-label">Keep Exploring</div>
      <h2 class="s-title">You Might Also Like</h2>
    </div>
    <div class="rel-grid">
{related_cards(slug)}
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="assets/logo.png" alt="Modern Home Blinds" style="height:48px"/>
        <p>Canadian owned &amp; operated. Custom window coverings manufactured in Oakville, ON. We measure, manufacture, and install &mdash; so you don&rsquo;t have to lift a finger.</p>
        <div class="footer-rating">&#9733;&#9733;&#9733;&#9733;&#9733; <strong>5.0</strong> on Google &nbsp;&middot;&nbsp; 10,000+ Clients</div>
      </div>
      <div class="footer-col"><h4>Products</h4><ul>
{footer_products()}
      </ul></div>
      <div class="footer-col"><h4>Locations</h4><ul>
        <li><a href="index.html">Oakville</a></li><li><a href="index.html">Milton</a></li>
        <li><a href="index.html">Mississauga</a></li><li><a href="index.html">Brampton</a></li>
        <li><a href="index.html">Burlington</a></li><li><a href="index.html">Toronto</a></li>
      </ul></div>
      <div class="footer-col"><h4>Contact</h4><ul>
        <li><a href="tel:{PHONE_TEL}">&#128222; {PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">&#128231; {EMAIL}</a></li>
        <li><span>&#127981; Made in Oakville, ON</span></li>
        <li><a href="https://www.facebook.com/profile.php?id=61571563192062" target="_blank">Facebook</a></li>
        <li><a href="https://www.instagram.com/exaadecor/" target="_blank">Instagram</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Modern Home Blinds. All rights reserved. Canadian Owned &amp; Operated. Manufactured in Oakville, ON. Serving the Greater Toronto Area.</p>
    </div>
  </div>
</footer>

<script>
function toggleNav(){{document.getElementById('navLinks').classList.toggle('open')}}
document.querySelectorAll('.has-drop > a').forEach(function(a){{
  a.addEventListener('click',function(e){{if(window.innerWidth<=960){{e.preventDefault();a.parentElement.classList.toggle('open')}}}})
}})
function toggleFaq(btn){{
  var a=btn.nextElementSibling
  var isOpen=a.classList.contains('open')
  document.querySelectorAll('.faq-a').forEach(function(x){{x.classList.remove('open')}})
  document.querySelectorAll('.faq-q').forEach(function(x){{x.classList.remove('open')}})
  if(!isOpen){{a.classList.add('open');btn.classList.add('open')}}
}}
</script>
</body>
</html>
'''


def strip_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', s).replace('&amp;', '&').replace('&ndash;', '-').replace('&middot;', '·').replace('&mdash;', '—').replace('“', '"').replace('”', '"')


def json_str(s):
    import json
    return json.dumps(s)


if __name__ == "__main__":
    for slug, p in PRODUCTS.items():
        out = render(slug, p)
        with open(f"{slug}.html", "w", encoding="utf-8") as f:
            f.write(out)
        print("wrote", f"{slug}.html")
