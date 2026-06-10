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
    ("california-shutters", "California Shutters"),
    ("silhouette-shades", "Silhouette Shades"),
    ("cellular-shades", "Cellular Shades"),
    ("draperies-sheers", "Draperies & Sheers"),
    ("motorized-blinds", "Motorized Blinds"),
    ("soft-vertical-blinds", "Soft Vertical Blinds"),
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
            ("&#9881;", "Motorized Option", "Add quiet Somfy motorization with remote, app and voice control."),
        ],
        specs=[("100+", "Fabric &amp; colour options"), ("1 wk", "Typical install time"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#127869;", "Kitchen"), ("&#128716;", "Bedroom"),
               ("&#127968;", "Home Office"), ("&#128701;", "Bathroom"), ("&#127970;", "Condos"),
               ("&#127797;", "Sunrooms"), ("&#127859;", "Dining Room")],
        faqs=[
            ("What exactly are zebra blinds?", "Zebra blinds combine alternating sheer and solid horizontal fabric bands on one roller mechanism. As you raise or lower the shade the bands shift, letting you switch between a clear view, filtered light, or full privacy."),
            ("Do zebra blinds give full privacy at night?", "Yes. When the solid bands are aligned they block the view inside. For bedrooms or street-facing windows we can also pair them with a blackout roller for total darkness."),
            ("Can zebra blinds be motorized?", "Absolutely. We offer quiet Somfy motors with remote, smartphone app and voice control (Alexa, Google Home, Apple HomeKit) — perfect for large or hard-to-reach windows."),
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
            ("Motor-ready", "Upgrade to Somfy motorization for one-touch or scheduled control."),
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
            ("Can roller shades be motorized?", "Yes — our roller shades accept quiet Somfy motors controlled by remote, smartphone app, schedules, or voice assistants."),
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
        h1=("<em>Motorized &amp; Smart</em> Blinds — Powered by Somfy"),
        pill="Smart Home Ready",
        title="Motorized Blinds GTA | Somfy Smart Shades — Modern Home Blinds",
        desc="Motorized and smart blinds for the GTA, powered by Somfy. App, remote and voice control with scheduling. Perfect for high windows. Free in-home consultation.",
        sub="Open and close your shades with a tap, a voice command, or on an automatic schedule. Whisper-quiet Somfy motors bring effortless control to every window — even the ones you can't reach.",
        price=None,
        price_note="Motorization adds roughly $200 per window over manual pricing.",
        ov_title="Your windows, fully automated",
        ov_p=[
            "Motorized blinds remove the cords and the effort. With reliable Somfy motors you can raise and lower shades from a remote, your phone, or a simple voice command to Alexa, Google Home or Apple HomeKit. Set schedules so blinds wake with the sun and close at dusk — saving energy and adding security while you're away.",
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
            ("&#9889;", "Somfy Powered", "Reliable, whisper-quiet motors from the global leader."),
            ("&#9201;", "Schedule Automation", "Open and close automatically around your daily routine."),
            ("&#128205;", "Great for High Windows", "Effortless control of tall and hard-to-reach openings."),
            ("&#127807;", "Energy Saving", "Automate shades to reduce heating and cooling loads."),
            ("&#128274;", "Added Security", "Scheduled movement makes your home look lived-in."),
        ],
        specs=[("Somfy", "Motor technology"), ("Battery / Wired", "Power options"),
               ("5.0&#9733;", "Average Google rating"), ("Free", "In-home consultation")],
        rooms=[("&#128719;", "Living Room"), ("&#128716;", "Bedroom"), ("&#127968;", "Home Office"),
               ("&#127970;", "Condos"), ("&#127797;", "Sunrooms"), ("&#128205;", "High Windows"),
               ("&#127902;", "Media Room"), ("&#127869;", "Kitchen")],
        faqs=[
            ("Which blinds can be motorized?", "Almost all of them — zebra blinds, roller and solar shades, Roman shades, cellular shades, sheers and even drapery tracks can be motorized with Somfy motors."),
            ("Do motorized blinds need to be hardwired?", "Not necessarily. Most of our motors are rechargeable-battery powered, so no electrician is required. Hardwired options are available for new builds or permanent installations."),
            ("Can I control them with my voice or phone?", "Yes. With a Somfy hub you can control shades from a smartphone app and through Alexa, Google Home and Apple HomeKit, plus set automatic schedules and scenes."),
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
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="https://www.modernhomeblinds.ca/{slug}.html"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500;1,9..144,600&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="assets/product.css"/>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_ld}]}}
</script>
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
