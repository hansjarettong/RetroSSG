# 💾 RetroSSG (Retro Static Site Generator)

A lightweight, custom-built Python Static Site Generator (SSG) designed to programmatically generate vintage, 90s-style websites. 

Instead of relying on heavy modern frameworks, this project uses a custom Python compilation engine to parse YAML configurations and inject content into reusable HTML templates. It also includes a custom image processing tool to ensure all visual assets match the retro aesthetic.

## ✨ Features

* **YAML-Driven Architecture:** The entire site hierarchy, page variables, and template inheritance are defined centrally in `site-template.yaml`.
* **Custom Templating Engine:** The `compile_site.py` script recursively parses base and child templates, dynamically replacing `{{variable}}` tags with raw HTML or mapped strings.
* **Dynamic HTML Generation:** The engine detects nested dictionaries in the YAML config and automatically translates them into properly formatted HTML unordered lists (`<ul>` and `<li>`), which is used to generate the site's retro file explorer structures.
* **Image Retrofier CLI:** A built-in Python tool (`image_retrofier.py`) that downgrades modern, high-resolution images. It calculates resolution scaling (defaulting to a 640x480 ratio) and reduces the color palette via bit-depth reduction (e.g., 8-bit / 256 colors) using an adaptive palette to perfectly simulate early web graphics.

## 📁 Project Structure

\`\`\`text
├── template/
│   ├── compile_site.py        # The core SSG compilation script
│   ├── site-template.yaml     # The master configuration for site structure
│   ├── base.template          # The base HTML template
│   ├── file-explorer.template # Child template for recursive rendering
│   └── content/               # Raw HTML fragments (index, cv, research)
├── tools/
│   └── image_retrofier.py     # CLI tool for downscaling image resolution/colors
└── build/                     # The compiled, deployable static site (generated automatically)
\`\`\`

## 🚀 Usage

### 1. Requirements
Ensure you have Python 3 installed along with the required dependencies:
\`\`\`bash
pip install PyYAML Pillow
\`\`\`

### 2. Building the Site
To compile the static site from the templates and YAML configuration, simply run the compiler script:
\`\`\`bash
python template/compile_site.py
\`\`\`
The generated HTML files will be automatically output to the `build/` directory, ready to be hosted on GitHub Pages, Netlify, or any static file server.

### 3. Retrofying Images
To convert a modern image to a retro aesthetic, use the included CLI tool:
\`\`\`bash
python tools/image_retrofier.py <input_image_path> <output_image_path> [bit_depth] [resolution_width] [resolution_height]
\`\`\`
**Example:**
\`\`\`bash
python tools/image_retrofier.py assets/modern_headshot.jpg assets/retro_headshot.png 8 640 480
\`\`\`
*(If bit depth and resolution are omitted, the tool defaults to 8-bit and 640x480.)*
