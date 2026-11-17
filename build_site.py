#!/usr/bin/env python3
"""
Zyntara Website Builder
Unifies all extracted Stitch pages into a cohesive, high-performance,
production-ready multi-page website with shared navigation, active indicators,
smooth interactive components, SEO metadata, and zero broken links.
"""

import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'extracted_raw', 'stitch_zyntara_ai_agency_landing_page')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
SCREENSHOTS_DIR = os.path.join(ASSETS_DIR, 'screenshots')

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, 'js'), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, 'css'), exist_ok=True)

PAGE_MAPPING = [
    {
        'src_dir': 'zyntara_premium_ai_digital_growth_agency_landing_page',
        'out_file': 'index.html',
        'page_id': 'home',
        'title': 'Zyntara — AI-Powered Digital Growth Agency | High-Performing Conversions & Automation',
        'desc': 'Zyntara combines high-performing conversion websites, algorithmic marketing, SEO/GEO/AEO, and autonomous AI pipelines to flood your business with high-value leads.',
    },
    {
        'src_dir': 'zyntara_about_us_modern_growth_ai_agency',
        'out_file': 'about.html',
        'page_id': 'about',
        'title': 'About Zyntara — Modern Growth & AI Automation Agency',
        'desc': 'Discover Zyntara’s mission, engineering approach, and multidisciplinary team building the next generation of algorithmic growth systems and autonomous AI pipelines.',
    },
    {
        'src_dir': 'zyntara_premium_ai_digital_growth_agency',
        'out_file': 'services.html',
        'page_id': 'services',
        'title': 'Services & Growth Solutions Hub — Zyntara AI Systems',
        'desc': 'Explore our full suite of enterprise digital growth services: web and mobile engineering, SEO, GEO, AEO, paid acquisition, and custom autonomous AI pipelines.',
    },
    {
        'src_dir': 'zyntara_ai_solutions_autonomous_automation_agents',
        'out_file': 'ai-solutions.html',
        'page_id': 'ai-solutions',
        'title': 'Autonomous AI Agents & Intelligent Automation Solutions — Zyntara',
        'desc': 'Deploy 24/7 intelligent voice agents, conversational chatbots, autonomous lead qualification, and end-to-end automated business workflows with Zyntara.',
    },
    {
        'src_dir': 'zyntara_website_development_services',
        'out_file': 'web-development.html',
        'page_id': 'web-dev',
        'title': 'High-Converting Website Development Services — Zyntara',
        'desc': 'Conversion-engineered websites and web portals built with cutting-edge architectures, blazing speeds, and relentless conversion optimization.',
    },
    {
        'src_dir': 'zyntara_application_development_services',
        'out_file': 'app-development.html',
        'page_id': 'app-dev',
        'title': 'Custom Application Development & Cloud Software — Zyntara',
        'desc': 'Robust, scalable web applications, mobile platforms, and internal enterprise tools built with cloud-native resilience and intuitive UX.',
    },
    {
        'src_dir': 'zyntara_digital_marketing_services',
        'out_file': 'digital-marketing.html',
        'page_id': 'digital-marketing',
        'title': 'Algorithmic Digital Marketing & Multi-Channel Growth — Zyntara',
        'desc': 'Data-backed multi-channel digital marketing campaigns that turn audience attention into measurable customer acquisition and compounding revenue.',
    },
    {
        'src_dir': 'zyntara_organic_seo_search_visibility_services',
        'out_file': 'seo-services.html',
        'page_id': 'seo',
        'title': 'Organic SEO & High-Intent Search Visibility Services — Zyntara',
        'desc': 'Dominate high-intent search queries and compound organic traffic with technical SEO audits, programmatic content architecture, and authority building.',
    },
    {
        'src_dir': 'zyntara_generative_engine_optimization_geo_services',
        'out_file': 'geo-services.html',
        'page_id': 'geo',
        'title': 'Generative Engine Optimization (GEO) Services — Zyntara',
        'desc': 'Ensure your brand is recommended and cited across AI answer engines including ChatGPT, Perplexity, Claude, and Gemini with cutting-edge GEO.',
    },
    {
        'src_dir': 'zyntara_answer_engine_optimization_aeo_services',
        'out_file': 'aeo-services.html',
        'page_id': 'aeo',
        'title': 'Answer Engine Optimization (AEO) Services — Zyntara',
        'desc': 'Capture voice search, direct answer boxes, and zero-click answer engines with conversational schema structuring and factual entity mapping.',
    },
    {
        'src_dir': 'zyntara_meta_ads_facebook_instagram_management_services',
        'out_file': 'meta-ads.html',
        'page_id': 'meta-ads',
        'title': 'High-ROAS Meta Ads Management (Facebook & Instagram) — Zyntara',
        'desc': 'Performance-driven Facebook and Instagram ad management with creative testing engines, dynamic audience modeling, and proven full-funnel conversion systems.',
    },
    {
        'src_dir': 'zyntara_google_ads_management_services',
        'out_file': 'google-ads.html',
        'page_id': 'google-ads',
        'title': 'Google Ads Management Services (Search, PMax, YouTube) — Zyntara',
        'desc': 'Capture high-intent in-market buyers at the moment of intent with Google Search, Performance Max, and YouTube ad campaigns optimized for profitability.',
    },
    {
        'src_dir': 'zyntara_insights_practical_growth_blog',
        'out_file': 'blog.html',
        'page_id': 'blog',
        'title': 'Practical Growth & AI Insights — Zyntara Blog',
        'desc': 'Actionable frameworks, real-world case studies, and engineering deep dives on AI automation, GEO, performance marketing, and digital scale.',
    },
    {
        'src_dir': 'zyntara_contact_us_let_s_discuss_your_growth',
        'out_file': 'contact.html',
        'page_id': 'contact',
        'title': 'Contact Zyntara — Let’s Discuss Your Growth Goals & Schedule Audit',
        'desc': 'Get in touch with Zyntara’s growth specialists. Book your free growth audit and discover how our AI pipelines and growth infrastructure can scale your business.',
    },
]

# Copy screenshot previews
if os.path.exists(SRC_DIR):
    for p in PAGE_MAPPING:
        src_screen = os.path.join(SRC_DIR, p['src_dir'], 'screen.png')
        if os.path.exists(src_screen):
            dst_screen = os.path.join(SCREENSHOTS_DIR, f"{p['out_file'].replace('.html', '.png')}")
            shutil.copy2(src_screen, dst_screen)

# SVG Favicon
FAVICON_SVG = """<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%236d28d9'/><stop offset='50%' stop-color='%235de6ff'/><stop offset='100%' stop-color='%23d3bbff'/></linearGradient></defs><rect width='100' height='100' rx='24' fill='%230f131e'/><path d='M25 30 L75 30 L38 70 L75 70' stroke='url(%23g)' stroke-width='10' stroke-linecap='round' stroke-linejoin='round' fill='none'/><circle cx='70' cy='30' r='5' fill='%235de6ff'/><circle cx='30' cy='70' r='5' fill='%236d28d9'/></svg>">"""

# Standard Tailwind config superset
TAILWIND_CONFIG_SCRIPT = """<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "surface": "#0f131e",
        "surface-dim": "#0f131e",
        "surface-bright": "#353946",
        "surface-container-lowest": "#0a0e19",
        "surface-container-low": "#171b27",
        "surface-container": "#1b1f2b",
        "surface-container-high": "#262a36",
        "surface-container-highest": "#303441",
        "surface-variant": "#303441",
        "surface-tint": "#d3bbff",
        "on-surface": "#dfe2f2",
        "on-surface-variant": "#ccc3d7",
        "inverse-surface": "#dfe2f2",
        "inverse-on-surface": "#2c303c",
        "outline": "#958da1",
        "outline-variant": "#4a4455",
        "primary": "#d3bbff",
        "on-primary": "#3f008d",
        "primary-container": "#6d28d9",
        "on-primary-container": "#dac5ff",
        "inverse-primary": "#7331df",
        "primary-fixed": "#ebddff",
        "primary-fixed-dim": "#d3bbff",
        "on-primary-fixed": "#250059",
        "on-primary-fixed-variant": "#5b00c5",
        "secondary": "#5de6ff",
        "on-secondary": "#00363e",
        "secondary-container": "#00cbe6",
        "on-secondary-container": "#00515d",
        "secondary-fixed": "#a2eeff",
        "secondary-fixed-dim": "#2fd9f4",
        "on-secondary-fixed": "#001f25",
        "on-secondary-fixed-variant": "#004e5a",
        "tertiary": "#ffb95f",
        "on-tertiary": "#472a00",
        "tertiary-container": "#7d4e00",
        "on-tertiary-container": "#ffc47d",
        "tertiary-fixed": "#ffddb8",
        "tertiary-fixed-dim": "#ffb95f",
        "on-tertiary-fixed": "#2a1700",
        "on-tertiary-fixed-variant": "#653e00",
        "error": "#ffb4ab",
        "on-error": "#690005",
        "error-container": "#93000a",
        "on-error-container": "#ffdad6",
        "background": "#0f131e",
        "on-background": "#dfe2f2"
      },
      borderRadius: {
        "DEFAULT": "1rem",
        "lg": "2rem",
        "xl": "3rem",
        "full": "9999px"
      },
      fontFamily: {
        "display-hero": ["Space Grotesk", "sans-serif"],
        "display-hero-mobile": ["Space Grotesk", "sans-serif"],
        "headline-xl": ["Space Grotesk", "sans-serif"],
        "headline-xl-mobile": ["Space Grotesk", "sans-serif"],
        "headline-lg": ["Space Grotesk", "sans-serif"],
        "headline-md": ["Space Grotesk", "sans-serif"],
        "headline-sm": ["Space Grotesk", "sans-serif"],
        "label-mono": ["Space Grotesk", "monospace"],
        "label-lg": ["Plus Jakarta Sans", "sans-serif"],
        "label-md": ["Plus Jakarta Sans", "sans-serif"],
        "body-lg": ["Plus Jakarta Sans", "sans-serif"],
        "body-md": ["Plus Jakarta Sans", "sans-serif"],
        "body-sm": ["Plus Jakarta Sans", "sans-serif"]
      }
    }
  }
};
</script>"""

def render_header(current_page_id):
    def active_class(page_id, is_sub=False):
        if is_sub:
            return "text-secondary font-semibold" if current_page_id == page_id else "text-on-surface-variant hover:text-on-surface"
        return "text-secondary bg-surface-container font-bold px-3 py-1.5 rounded-full" if current_page_id == page_id else "text-on-surface-variant hover:text-on-surface px-3 py-1.5 transition-colors"

    def mobile_active_class(page_id):
        return "text-secondary bg-surface-container font-bold px-4 py-3 rounded-lg" if current_page_id == page_id else "text-on-surface-variant hover:text-on-surface px-4 py-3 rounded-lg transition-colors"

    return f"""<header class="fixed top-0 left-0 right-0 z-50 bg-surface-container-lowest/80 backdrop-blur-xl border-b border-outline-variant/20 shadow-[0_1px_8px_rgba(0,0,0,0.4)]">
  <div class="h-20 max-w-7xl mx-auto px-6 lg:px-12 flex items-center justify-between gap-4">
    <!-- Brand Logo -->
    <a href="index.html" class="flex items-center gap-3 shrink-0 group">
      <img alt="Zyntara Logo" class="h-8 w-auto object-contain transition-transform duration-300 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida/ALJJyrCq9AlNczhf-jQxlMKyyd0OYbMoZBh_Df4x_UkceZ5NzeRu4Mc9Sni9_-9mOA-lT76uaFOXSkvKlVCnmq4sITcWZ22fOdyEMSj_liQSbLVQPHrsNzjN5csM08rgThw1jljuaFQpZp9HHlFjB4DREMTGKAM239ZJUMJr1yhXI6Vp4393YzT6yNg2JHm6lTyh2pAaMhVrLmn809jmxhs-uSCZLGI93kBnG2z-S_kAu3m1GQ">
      <span class="font-headline-sm text-headline-sm text-on-surface tracking-tight font-bold group-hover:text-secondary transition-colors hidden sm:inline-block">Zyntara</span>
    </a>

    <!-- Desktop Nav Items -->
    <nav class="hidden xl:flex items-center gap-1 bg-surface-container-low/70 px-3 py-1.5 rounded-full border border-outline-variant/30">
      <a class="{active_class('home')} font-label-lg text-label-lg" href="index.html">Home</a>
      
      <!-- Services Dropdown -->
      <div class="relative group">
        <a href="services.html" class="{active_class('services')} font-label-lg text-label-lg inline-flex items-center gap-1 focus:outline-none cursor-pointer">
          <span>Services</span>
          <span class="material-symbols-outlined text-[16px] transition-transform duration-200 group-hover:rotate-180">expand_more</span>
        </a>
        <div class="absolute top-full left-1/2 -translate-x-1/2 pt-3 w-[560px] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
          <div class="bg-surface-container-lowest/95 backdrop-blur-2xl border border-outline-variant/40 rounded-2xl p-4 shadow-[0_12px_40px_rgba(0,0,0,0.7)] grid grid-cols-2 gap-2">
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="ai-solutions.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">smart_toy</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">Complete AI Solutions</span><span class="font-label-mono text-[10px] text-on-surface-variant">24/7 AI Chatbots & Voice Agents</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="web-development.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">devices</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">Website Development</span><span class="font-label-mono text-[10px] text-on-surface-variant">High-conversion portals</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="app-development.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">code</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">Application Development</span><span class="font-label-mono text-[10px] text-on-surface-variant">Custom web & mobile apps</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="digital-marketing.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">campaign</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">Digital Marketing</span><span class="font-label-mono text-[10px] text-on-surface-variant">Multi-channel growth funnels</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="seo-services.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">trending_up</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">SEO Visibility</span><span class="font-label-mono text-[10px] text-on-surface-variant">Organic search dominance</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="geo-services.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">neurology</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">GEO Services</span><span class="font-label-mono text-[10px] text-on-surface-variant">Generative Engine Optimization</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="aeo-services.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">record_voice_over</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">AEO Services</span><span class="font-label-mono text-[10px] text-on-surface-variant">Answer Engine & voice search</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="meta-ads.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">ad_units</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">Meta Ads</span><span class="font-label-mono text-[10px] text-on-surface-variant">High-ROAS Facebook & IG</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item" href="google-ads.html">
              <div class="w-8 h-8 rounded-lg bg-surface-container-high flex items-center justify-center text-secondary group-hover/item:bg-primary-container/20"><span class="material-symbols-outlined text-[18px]">ads_click</span></div>
              <div><span class="block font-label-md text-label-md text-on-surface group-hover/item:text-secondary transition-colors font-semibold">Google Ads</span><span class="font-label-mono text-[10px] text-on-surface-variant">High-intent Search & PMax</span></div>
            </a>
            <a class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-surface-container transition-colors group/item border border-secondary/20 bg-secondary/5" href="services.html">
              <div class="w-8 h-8 rounded-lg bg-secondary/10 flex items-center justify-center text-secondary"><span class="material-symbols-outlined text-[18px]">hub</span></div>
              <div><span class="block font-label-md text-label-md text-secondary font-bold">Services Overview Hub</span><span class="font-label-mono text-[10px] text-on-surface-variant">All 9 pillars & matrix</span></div>
            </a>
          </div>
        </div>
      </div>

      <a class="{active_class('ai-solutions')} font-label-lg text-label-lg" href="ai-solutions.html">AI Solutions</a>
      <a class="{active_class('about')} font-label-lg text-label-lg" href="about.html">About Us</a>
      <a class="{active_class('blog')} font-label-lg text-label-lg" href="blog.html">Blog</a>
      <a class="{active_class('contact')} font-label-lg text-label-lg" href="contact.html">Contact Us</a>
    </nav>

    <!-- Header Actions -->
    <div class="flex items-center gap-3">
      <a class="hidden md:inline-flex items-center justify-center font-label-lg text-label-lg px-4 py-2.5 rounded-full bg-surface-container hover:bg-surface-container-high text-on-surface border border-outline-variant/30 transition-all hover:border-secondary/40" href="https://wa.me/?text=Hello%20Zyntara%20Team%2C%20I%20would%20like%20to%20learn%20more%20about%20your%20digital%20growth%20and%20AI%20services." target="_blank" rel="noopener noreferrer">
        <span class="material-symbols-outlined text-[17px] mr-1.5 text-secondary">chat</span>
        WhatsApp Us
      </a>
      <a class="hidden sm:inline-flex items-center justify-center font-label-lg text-label-lg px-5 py-2.5 rounded-full bg-gradient-to-r from-primary-container via-purple-600 to-secondary text-surface-container-lowest font-bold shadow-[0_0_24px_-4px_rgba(93,230,255,0.4)] hover:shadow-[0_0_30px_rgba(93,230,255,0.65)] hover:opacity-95 transition-all" href="contact.html#book-call">
        <span class="material-symbols-outlined text-[17px] mr-1.5">calendar_today</span>
        Book Free Strategy Call
      </a>
      <button aria-label="Toggle Navigation Menu" class="xl:hidden p-2 rounded-full bg-surface-container text-on-surface hover:bg-surface-container-high border border-outline-variant/40 flex items-center justify-center cursor-pointer transition-colors" id="mobile-menu-toggle">
        <span class="material-symbols-outlined" id="mobile-menu-icon">menu</span>
      </button>
    </div>
  </div>

  <!-- Mobile Nav Drawer -->
  <div class="hidden xl:hidden bg-surface-container-lowest/98 backdrop-blur-2xl border-b border-outline-variant/30 px-6 py-6 space-y-4 max-h-[85vh] overflow-y-auto" id="mobile-nav-drawer">
    <nav class="flex flex-col space-y-1">
      <a class="{mobile_active_class('home')}" href="index.html">Home</a>
      
      <div class="px-4 py-2 rounded-lg bg-surface-container-low/50">
        <div class="flex items-center justify-between cursor-pointer py-1" id="mobile-services-toggle">
          <span class="font-label-md text-label-md text-secondary uppercase font-bold tracking-wider">Services</span>
          <span class="material-symbols-outlined text-[18px] text-secondary transition-transform duration-200" id="mobile-services-arrow">expand_more</span>
        </div>
        <div class="hidden pt-2 pl-3 border-l border-outline-variant/40 space-y-2 mt-1" id="mobile-services-list">
          <a class="block font-body-sm text-body-sm {active_class('services', True)}" href="services.html">✦ All Services Overview Hub</a>
          <a class="block font-body-sm text-body-sm {active_class('ai-solutions', True)}" href="ai-solutions.html">Complete AI Solutions</a>
          <a class="block font-body-sm text-body-sm {active_class('web-dev', True)}" href="web-development.html">Website Development</a>
          <a class="block font-body-sm text-body-sm {active_class('app-dev', True)}" href="app-development.html">Application Development</a>
          <a class="block font-body-sm text-body-sm {active_class('digital-marketing', True)}" href="digital-marketing.html">Digital Marketing</a>
          <a class="block font-body-sm text-body-sm {active_class('seo', True)}" href="seo-services.html">SEO (Search Engine Optimization)</a>
          <a class="block font-body-sm text-body-sm {active_class('geo', True)}" href="geo-services.html">GEO (Generative Engine Optimization)</a>
          <a class="block font-body-sm text-body-sm {active_class('aeo', True)}" href="aeo-services.html">AEO (Answer Engine Optimization)</a>
          <a class="block font-body-sm text-body-sm {active_class('meta-ads', True)}" href="meta-ads.html">Meta Ads (Facebook & Instagram)</a>
          <a class="block font-body-sm text-body-sm {active_class('google-ads', True)}" href="google-ads.html">Google Ads (Search & PMax)</a>
        </div>
      </div>

      <a class="{mobile_active_class('ai-solutions')}" href="ai-solutions.html">AI Solutions</a>
      <a class="{mobile_active_class('about')}" href="about.html">About Us</a>
      <a class="{mobile_active_class('blog')}" href="blog.html">Blog & Insights</a>
      <a class="{mobile_active_class('contact')}" href="contact.html">Contact Us</a>
    </nav>
    <div class="pt-4 flex flex-col gap-2.5 sm:hidden border-t border-outline-variant/30">
      <a class="w-full text-center font-label-lg text-label-lg px-4 py-3 rounded-full bg-surface-container text-on-surface border border-outline-variant/40 flex items-center justify-center gap-2" href="https://wa.me/?text=Hello%20Zyntara%20Team%2C%20I%20would%20like%20to%20learn%20more%20about%20your%20digital%20growth%20and%20AI%20services." target="_blank" rel="noopener noreferrer">
        <span class="material-symbols-outlined text-[18px] text-secondary">chat</span>
        WhatsApp Us
      </a>
      <a class="w-full text-center font-label-lg text-label-lg px-4 py-3 rounded-full bg-gradient-to-r from-primary-container via-purple-600 to-secondary text-surface-container-lowest font-bold shadow-[0_0_24px_-4px_rgba(93,230,255,0.4)] flex items-center justify-center gap-2" href="contact.html#book-call">
        <span class="material-symbols-outlined text-[18px]">calendar_today</span>
        Book Free Strategy Call
      </a>
    </div>
  </div>
</header>"""

def render_footer():
    return """<footer class="w-full bg-surface-container-lowest py-16 border-t border-outline-variant/20 shadow-[0_-1px_12px_rgba(0,0,0,0.4)]">
  <div class="max-w-7xl mx-auto px-6 lg:px-12">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">
      <!-- Col 1: Brand Info -->
      <div class="space-y-4">
        <div class="flex items-center gap-3">
          <img alt="Zyntara Logo" class="h-7 w-auto object-contain" src="https://lh3.googleusercontent.com/aida/ALJJyrCq9AlNczhf-jQxlMKyyd0OYbMoZBh_Df4x_UkceZ5NzeRu4Mc9Sni9_-9mOA-lT76uaFOXSkvKlVCnmq4sITcWZ22fOdyEMSj_liQSbLVQPHrsNzjN5csM08rgThw1jljuaFQpZp9HHlFjB4DREMTGKAM239ZJUMJr1yhXI6Vp4393YzT6yNg2JHm6lTyh2pAaMhVrLmn809jmxhs-uSCZLGI93kBnG2z-S_kAu3m1GQ">
          <span class="font-headline-sm text-headline-sm text-on-surface font-bold tracking-tight">Zyntara</span>
        </div>
        <p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
          Enterprise AI automation, generative engine visibility (GEO/AEO), and autonomous digital growth infrastructure engineered for mission-critical business scale.
        </p>
        <div class="flex items-center gap-3 pt-2">
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-surface-container text-xs text-secondary font-mono border border-secondary/20">
            <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span> Systems Active 24/7
          </span>
        </div>
      </div>

      <!-- Col 2: Solutions -->
      <div>
        <h4 class="font-headline-sm text-headline-sm text-on-surface mb-4 font-semibold">Growth Solutions</h4>
        <ul class="space-y-2.5 font-body-sm text-body-sm text-on-surface-variant">
          <li><a class="hover:text-secondary transition-colors" href="ai-solutions.html">Autonomous AI Agents & Chatbots</a></li>
          <li><a class="hover:text-secondary transition-colors" href="web-development.html">High-Converting Web Development</a></li>
          <li><a class="hover:text-secondary transition-colors" href="app-development.html">Cloud Software & Mobile Apps</a></li>
          <li><a class="hover:text-secondary transition-colors" href="digital-marketing.html">Multi-Channel Digital Marketing</a></li>
          <li><a class="hover:text-secondary transition-colors" href="seo-services.html">Organic SEO Search Visibility</a></li>
          <li><a class="hover:text-secondary transition-colors" href="geo-services.html">Generative Engine Optimization (GEO)</a></li>
          <li><a class="hover:text-secondary transition-colors" href="aeo-services.html">Answer Engine Optimization (AEO)</a></li>
          <li><a class="hover:text-secondary transition-colors" href="meta-ads.html">Meta Ads (Facebook & Instagram)</a></li>
          <li><a class="hover:text-secondary transition-colors" href="google-ads.html">Google Ads (Search & PMax)</a></li>
          <li><a class="hover:text-secondary transition-colors font-semibold text-secondary" href="services.html">✦ All Services Directory</a></li>
        </ul>
      </div>

      <!-- Col 3: Agency & Company -->
      <div>
        <h4 class="font-headline-sm text-headline-sm text-on-surface mb-4 font-semibold">Agency</h4>
        <ul class="space-y-2.5 font-body-sm text-body-sm text-on-surface-variant">
          <li><a class="hover:text-secondary transition-colors" href="about.html">About Zyntara</a></li>
          <li><a class="hover:text-secondary transition-colors" href="services.html">Growth Methodology</a></li>
          <li><a class="hover:text-secondary transition-colors" href="blog.html">Case Studies & Insights</a></li>
          <li><a class="hover:text-secondary transition-colors" href="contact.html">Contact Us</a></li>
          <li><a class="hover:text-secondary transition-colors" href="contact.html#audit-section">Free Growth Audit</a></li>
          <li><a class="hover:text-secondary transition-colors" href="privacy.html">Privacy Framework</a></li>
          <li><a class="hover:text-secondary transition-colors" href="terms.html">Terms of Scale</a></li>
        </ul>
      </div>

      <!-- Col 4: Direct Access CTA -->
      <div>
        <h4 class="font-headline-sm text-headline-sm text-on-surface mb-4 font-semibold">Direct Access</h4>
        <p class="font-body-sm text-body-sm text-on-surface-variant mb-4 leading-relaxed">
          Ready to deploy quantum-leap growth systems and automate your inbound pipelines?
        </p>
        <div class="space-y-3">
          <a class="inline-flex items-center gap-2 font-label-md text-label-md text-secondary hover:text-on-surface transition-colors font-semibold bg-surface-container px-4 py-2.5 rounded-xl border border-secondary/20 hover:border-secondary/50 w-full justify-center" href="contact.html#book-call">
            <span class="material-symbols-outlined text-[18px]">calendar_today</span>
            Schedule Protocol Call
          </a>
          <a class="inline-flex items-center gap-2 font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors text-xs w-full justify-center" href="https://wa.me/?text=Hello%20Zyntara%20Team%2C%20I%20would%20like%20to%20learn%20more%20about%20your%20digital%20growth%20and%20AI%20services." target="_blank" rel="noopener noreferrer">
            <span class="material-symbols-outlined text-[16px]">chat</span>
            Direct WhatsApp Hotline
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="pt-8 border-t border-outline-variant/20 flex flex-col sm:flex-row items-center justify-between gap-4 font-body-sm text-body-sm text-on-surface-variant">
      <p>© 2026 Zyntara AI Systems. Engineered for autonomous business growth.</p>
      <div class="flex items-center gap-6">
        <a class="hover:text-secondary transition-colors text-xs" href="privacy.html">Privacy Framework</a>
        <a class="hover:text-secondary transition-colors text-xs" href="terms.html">Terms of Scale</a>
        <a class="hover:text-secondary transition-colors text-xs" href="contact.html">Security Protocol</a>
      </div>
    </div>
  </div>
</footer>"""

def render_mobile_bar():
    return """<div class="md:hidden fixed bottom-4 left-4 right-4 z-40 bg-surface-container-high/95 backdrop-blur-xl p-2 rounded-full border border-outline-variant/40 shadow-[0_4px_24px_rgba(0,0,0,0.6)] flex items-center gap-2">
  <a class="flex-1 text-center font-label-md text-label-md py-2.5 px-3 rounded-full bg-surface-container text-on-surface flex items-center justify-center gap-1.5 border border-outline-variant/30 hover:bg-surface-container-highest transition-colors" href="https://wa.me/?text=Hello%20Zyntara%20Team%2C%20I%20would%20like%20to%20learn%20more%20about%20your%20digital%20growth%20and%20AI%20services." target="_blank" rel="noopener noreferrer">
    <span class="material-symbols-outlined text-[16px] text-secondary">chat</span>
    <span>WhatsApp</span>
  </a>
  <a class="flex-1 text-center font-label-md text-label-md py-2.5 px-3 rounded-full bg-gradient-to-r from-primary-container via-purple-600 to-secondary text-surface-container-lowest font-bold flex items-center justify-center gap-1.5 shadow-[0_0_16px_rgba(93,230,255,0.35)] hover:opacity-95 transition-all" href="contact.html#book-call">
    <span class="material-symbols-outlined text-[16px]">bolt</span>
    <span>Strategy Call</span>
  </a>
</div>"""

SHARED_SCRIPTS = """<!-- Core Interactive Scripts -->
<script>
// Mobile Navigation Drawer Toggle
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-nav-drawer');
  const menuIcon = document.getElementById('mobile-menu-icon');
  
  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isHidden = drawer.classList.toggle('hidden');
      if (menuIcon) {
        menuIcon.textContent = isHidden ? 'menu' : 'close';
      }
    });

    // Close when clicking any link inside drawer
    drawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        drawer.classList.add('hidden');
        if (menuIcon) menuIcon.textContent = 'menu';
      });
    });
  }

  // Mobile Services Submenu Toggle
  const servicesToggle = document.getElementById('mobile-services-toggle');
  const servicesList = document.getElementById('mobile-services-list');
  const servicesArrow = document.getElementById('mobile-services-arrow');
  if (servicesToggle && servicesList) {
    servicesToggle.addEventListener('click', () => {
      servicesList.classList.toggle('hidden');
      if (servicesArrow) {
        servicesArrow.classList.toggle('rotate-180');
      }
    });
  }

  // FAQ Accordion Handlers
  document.querySelectorAll('.faq-toggle, [data-faq-toggle]').forEach(button => {
    button.addEventListener('click', (e) => {
      e.preventDefault();
      const item = button.closest('.faq-item') || button.parentElement;
      const content = item.querySelector('.faq-content') || item.querySelector('[data-faq-content]') || item.nextElementSibling;
      const icon = item.querySelector('.faq-icon') || item.querySelector('.material-symbols-outlined');
      if (!content) return;
      
      const isCurrentlyHidden = content.classList.contains('hidden');

      // Close all siblings
      const parentContainer = item.closest('.faq-container') || item.parentElement;
      if (parentContainer) {
        parentContainer.querySelectorAll('.faq-content, [data-faq-content]').forEach(c => c.classList.add('hidden'));
        parentContainer.querySelectorAll('.faq-icon').forEach(ic => ic.classList.remove('rotate-180'));
      }

      // Open selected
      if (isCurrentlyHidden) {
        content.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      }
    });
  });

  // Interactive Form Submissions (Audit and Contact Forms)
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : 'Submit';

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = `
          <span class="inline-flex items-center gap-2">
            <svg class="animate-spin h-4 w-4 text-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
            </svg>
            Transmitting Protocol...
          </span>
        `;
      }

      setTimeout(() => {
        // Success Notification Banner
        const toast = document.createElement('div');
        toast.className = 'fixed top-24 right-6 z-50 bg-surface-container-high border border-secondary text-on-surface p-4 rounded-2xl shadow-[0_8px_32px_rgba(93,230,255,0.4)] flex items-center gap-3 transition-all duration-300 transform translate-y-0';
        toast.innerHTML = `
          <div class="w-8 h-8 rounded-full bg-secondary/20 flex items-center justify-center text-secondary shrink-0">
            <span class="material-symbols-outlined text-[20px]">check_circle</span>
          </div>
          <div>
            <div class="font-headline-sm text-sm font-bold text-on-surface">Growth Inquiry Confirmed</div>
            <div class="font-body-sm text-xs text-on-surface-variant">A Senior AI Strategist will analyze your metrics and contact you within 24 hours.</div>
          </div>
        `;
        document.body.appendChild(toast);

        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
        form.reset();

        setTimeout(() => {
          toast.style.opacity = '0';
          toast.style.transform = 'translateY(-10px)';
          setTimeout(() => toast.remove(), 400);
        }, 5000);
      }, 900);
    });
  });
});
</script>"""

def fix_content_links(html, current_page_id):
    # Fix service grid CTA buttons on index.html
    html = re.sub(r'href="#services-grid"', 'href="services.html"' if current_page_id != 'home' else 'href="#services-grid"', html)
    html = re.sub(r'href="#audit-section"', 'href="contact.html#audit-section"' if current_page_id != 'home' else 'href="#audit-section"', html)
    html = re.sub(r'href="#ai-solutions-section"', 'href="ai-solutions.html"', html)
    html = re.sub(r'href="/application-development"', 'href="app-development.html"', html)
    html = re.sub(r'href="/aeo"', 'href="aeo-services.html"', html)
    html = re.sub(r'href="#website-development"', 'href="web-development.html"', html)
    html = re.sub(r'href="#about-us"', 'href="about.html"', html)
    html = re.sub(r'href="#case-studies"', 'href="blog.html"', html)
    html = re.sub(r'href="https://wa.me/yourphonenumber"', 'href="https://wa.me/?text=Hello%20Zyntara%20Team%2C%20I%20would%20like%20to%20learn%20more%20about%20your%20digital%20growth%20and%20AI%20services."', html)

    # In index.html services cards, replace generic links with direct target pages
    if current_page_id == 'home':
        # Card 1: Digital Marketing
        html = re.sub(
            r'(<h3[^>]*>Digital Marketing</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1digital-marketing.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 2: Website Development
        html = re.sub(
            r'(<h3[^>]*>Website Development</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1web-development.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 3: SEO
        html = re.sub(
            r'(<h3[^>]*>Search Engine Optimization.*?</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1seo-services.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 4: GEO
        html = re.sub(
            r'(<h3[^>]*>GEO.*?</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1geo-services.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 5: AEO
        html = re.sub(
            r'(<h3[^>]*>AEO.*?</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1aeo-services.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 6: AI Solutions
        html = re.sub(
            r'(<h3[^>]*>Complete AI Solutions</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1ai-solutions.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 7: Meta Ads
        html = re.sub(
            r'(<h3[^>]*>Meta Ads</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1meta-ads.html\2',
            html,
            flags=re.DOTALL
        )
        # Card 8: Google Ads
        html = re.sub(
            r'(<h3[^>]*>Google Ads</h3>.*?<a[^>]+href=")[^"]*(")',
            r'\1google-ads.html\2',
            html,
            flags=re.DOTALL
        )

    # Fix generic data-path buttons
    html = re.sub(r'data-path="book-strategy-call"\s+href="#"', 'href="contact.html#book-call"', html)
    html = re.sub(r'data-path="whatsapp"\s+href="#"', 'href="https://wa.me/?text=Hello%20Zyntara%20Team%2C%20I%20would%20like%20to%20learn%20more%20about%20your%20digital%20growth%20and%20AI%20services."', html)
    html = re.sub(r'data-path="home"\s+href="#"', 'href="index.html"', html)
    html = re.sub(r'data-path="about-us"\s+href="#"', 'href="about.html"', html)
    html = re.sub(r'data-path="ai-solutions"\s+href="#"', 'href="ai-solutions.html"', html)
    html = re.sub(r'data-path="blog"\s+href="#"', 'href="blog.html"', html)
    html = re.sub(r'data-path="contact"\s+href="#"', 'href="contact.html"', html)
    html = re.sub(r'data-path="services"\s+href="#"', 'href="services.html"', html)
    html = re.sub(r'data-path="privacy-policy"\s+href="#"', 'href="privacy.html"', html)
    html = re.sub(r'data-path="terms-of-service"\s+href="#"', 'href="terms.html"', html)

    return html

def build_page(page_def):
    src_file = os.path.join(SRC_DIR, page_def['src_dir'], 'code.html')
    with open(src_file, 'r', encoding='utf-8') as f:
        raw_html = f.read()

    # Extract main section
    main_match = re.search(r'<main[^>]*>(.*?)</main>', raw_html, re.DOTALL)
    if not main_match:
        raise ValueError(f"Could not extract <main> from {src_file}")
    main_content = main_match.group(1)

    # Extract any extra inline scripts (excluding duplicate menu scripts)
    extra_scripts = []
    for sc in re.finditer(r'<script>(.*?)</script>', raw_html, re.DOTALL):
        s_body = sc.group(1)
        if 'mobile-menu-toggle' in s_body or 'tailwind.config' in s_body:
            continue
        extra_scripts.append(f"<script>{s_body}</script>")

    current_page_id = page_def['page_id']
    main_content = fix_content_links(main_content, current_page_id)

    header_html = render_header(current_page_id)
    footer_html = render_footer()
    mobile_bar_html = render_mobile_bar()

    full_page = f"""<!DOCTYPE html>
<html class="dark scroll-smooth" lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_def['title']}</title>
  <meta name="description" content="{page_def['desc']}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{page_def['title']}">
  <meta property="og:description" content="{page_def['desc']}">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page_def['title']}">
  <meta name="twitter:description" content="{page_def['desc']}">

  {FAVICON_SVG}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">

  <style>
    @layer base {{
      html, body {{
        margin: 0;
        padding: 0;
      }}
      body {{
        overscroll-behavior: none;
      }}
      main > :first-child {{
        margin-top: 0 !important;
      }}
      main > :last-child {{
        margin-bottom: 0 !important;
      }}
    }}
    /* Custom sleek scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0f131e;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #262a36;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #353946;
    }}
  </style>

  {TAILWIND_CONFIG_SCRIPT}
</head>
<body class="bg-background font-body-md text-on-surface antialiased selection:bg-primary-container selection:text-on-primary-container min-h-screen flex flex-col">
  {header_html}

  <main class="w-full pt-20 bg-background flex-1 pb-24 md:pb-0">
    <div class="flex flex-col w-full text-on-surface antialiased overflow-hidden">
      {main_content}
    </div>
  </main>

  {mobile_bar_html}
  {footer_html}

  {''.join(extra_scripts)}
  {SHARED_SCRIPTS}
</body>
</html>
"""
    out_path = os.path.join(BASE_DIR, page_def['out_file'])
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(full_page)
    print(f"Generated {page_def['out_file']} ({len(full_page)} bytes)")

# Generate Privacy Policy Page
def build_privacy_page():
    content = """
<section class="relative w-full px-6 lg:px-12 pt-16 pb-24 max-w-5xl mx-auto">
  <div class="space-y-6">
    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-surface-container-high border border-outline-variant/30">
      <span class="w-2 h-2 rounded-full bg-secondary"></span>
      <span class="font-label-mono text-label-mono text-secondary tracking-widest uppercase font-semibold">Security & Data Governance</span>
    </div>
    <h1 class="font-display-hero text-headline-xl md:text-display-hero font-bold text-on-surface">Privacy Framework</h1>
    <p class="font-body-lg text-body-lg text-on-surface-variant">Last updated: November 2026</p>
    
    <div class="pt-8 space-y-8 text-on-surface-variant font-body-md leading-relaxed border-t border-outline-variant/30">
      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">1. Commitment to Data Integrity</h2>
        <p>At Zyntara AI Systems ("Zyntara"), we treat corporate data, growth metrics, and customer lead information as mission-critical enterprise assets. This Privacy Framework details how our automated infrastructure processes, encrypts, and isolates your digital information.</p>
      </div>

      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">2. Information Collection in AI & Growth Operations</h2>
        <p>We collect information strictly necessary to engineer conversion assets, execute algorithmic campaigns, and configure autonomous AI pipelines:</p>
        <ul class="list-disc pl-6 space-y-2">
          <li><strong>Audit Inquiries:</strong> Company URL, contact email, traffic metrics, and business operational objectives submitted via our growth forms.</li>
          <li><strong>Autonomous Pipeline Data:</strong> Anonymized interaction logs and qualification parameters utilized to calibrate AI chatbots and voice agents.</li>
          <li><strong>Analytics & Telemetry:</strong> Anonymized performance signals to measure conversion rates and Core Web Vitals optimization.</li>
        </ul>
      </div>

      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">3. Strict Isolation & Zero Unconsented Training</h2>
        <p>Client proprietary data and lead records are strictly siloed. Zyntara never sells, rents, or leverages proprietary client dataset records to train public third-party commercial LLM models without explicit bilateral enterprise consensus.</p>
      </div>

      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">4. Inquiries & Contact</h2>
        <p>For data governance requests or privacy inquiries, contact our security office at <a href="contact.html" class="text-secondary hover:underline font-semibold">our direct contact hub</a>.</p>
      </div>
    </div>
  </div>
</section>
"""
    p_def = {
        'out_file': 'privacy.html',
        'page_id': 'privacy',
        'title': 'Privacy Framework — Zyntara AI Systems',
        'desc': 'Zyntara Privacy Framework and enterprise data governance standards for AI automation and growth operations.'
    }
    header = render_header('privacy')
    footer = render_footer()
    mobile = render_mobile_bar()
    full = f"""<!DOCTYPE html>
<html class="dark scroll-smooth" lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p_def['title']}</title>
  <meta name="description" content="{p_def['desc']}">
  {FAVICON_SVG}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
  {TAILWIND_CONFIG_SCRIPT}
</head>
<body class="bg-background font-body-md text-on-surface antialiased min-h-screen flex flex-col">
  {header}
  <main class="w-full pt-20 bg-background flex-1 pb-24 md:pb-0">{content}</main>
  {mobile}
  {footer}
  {SHARED_SCRIPTS}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'privacy.html'), 'w') as f:
        f.write(full)
    print("Generated privacy.html")

# Build all mapped pages if source files exist
if os.path.exists(SRC_DIR):
    for p in PAGE_MAPPING:
        build_page(p)

    build_privacy_page()
    build_terms_page()
    build_404_page()

# Generate Terms of Scale Page
def build_terms_page():
    content = """
<section class="relative w-full px-6 lg:px-12 pt-16 pb-24 max-w-5xl mx-auto">
  <div class="space-y-6">
    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-surface-container-high border border-outline-variant/30">
      <span class="w-2 h-2 rounded-full bg-secondary"></span>
      <span class="font-label-mono text-label-mono text-secondary tracking-widest uppercase font-semibold">Service Architecture</span>
    </div>
    <h1 class="font-display-hero text-headline-xl md:text-display-hero font-bold text-on-surface">Terms of Scale</h1>
    <p class="font-body-lg text-body-lg text-on-surface-variant">Last updated: November 2026</p>
    
    <div class="pt-8 space-y-8 text-on-surface-variant font-body-md leading-relaxed border-t border-outline-variant/30">
      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">1. Agreement to Terms</h2>
        <p>By engaging Zyntara AI Systems ("Zyntara", "we", "us") or accessing our websites, software assets, and AI services, you agree to these Terms of Scale. These terms govern the deployment of conversion websites, autonomous AI pipelines, and digital marketing advisory.</p>
      </div>

      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">2. Service Delivery & Strategic Sprints</h2>
        <p>Zyntara operates on phased engineering sprints and milestone verification. While algorithmic strategies and AI automation are designed for compounding impact, individual business results scale with market demand, ad spend allocation, and operational responsiveness.</p>
      </div>

      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">3. Intellectual Property Rights</h2>
        <p>Upon fulfillment of contractual agreements, clients retain full ownership of bespoke frontend assets, customized brand collateral, and customer datasets engineered specifically for their entity.</p>
      </div>

      <div class="bg-surface-container-low p-8 rounded-3xl border border-outline-variant/30 space-y-4">
        <h2 class="font-headline-md text-headline-md text-on-surface font-semibold">4. Service Questions</h2>
        <p>For questions regarding enterprise engagements, reach our team via <a href="contact.html" class="text-secondary hover:underline font-semibold">our contact protocol</a>.</p>
      </div>
    </div>
  </div>
</section>
"""
    header = render_header('terms')
    footer = render_footer()
    mobile = render_mobile_bar()
    full = f"""<!DOCTYPE html>
<html class="dark scroll-smooth" lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Scale — Zyntara AI Systems</title>
  <meta name="description" content="Terms of Scale governing Zyntara AI Systems digital growth, engineering, and automation services.">
  {FAVICON_SVG}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
  {TAILWIND_CONFIG_SCRIPT}
</head>
<body class="bg-background font-body-md text-on-surface antialiased min-h-screen flex flex-col">
  {header}
  <main class="w-full pt-20 bg-background flex-1 pb-24 md:pb-0">{content}</main>
  {mobile}
  {footer}
  {SHARED_SCRIPTS}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'terms.html'), 'w') as f:
        f.write(full)
    print("Generated terms.html")

# Generate 404 Page
def build_404_page():
    content = """
<section class="relative w-full px-6 lg:px-12 py-32 max-w-4xl mx-auto text-center flex flex-col items-center justify-center space-y-6">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-surface-container-high border border-secondary/30">
    <span class="w-2 h-2 rounded-full bg-error animate-ping"></span>
    <span class="font-label-mono text-label-mono text-secondary tracking-widest uppercase font-semibold">Error 404 • Coordinate Void</span>
  </div>
  <h1 class="font-display-hero text-6xl md:text-8xl font-bold text-on-surface">404</h1>
  <p class="font-body-lg text-body-lg text-on-surface-variant max-w-lg mx-auto">
    The algorithmic growth route you are attempting to access does not exist or has been shifted in the network topology.
  </p>
  <div class="flex flex-wrap items-center justify-center gap-4 pt-4">
    <a href="index.html" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-gradient-to-r from-primary-container via-purple-600 to-secondary text-surface-container-lowest font-bold shadow-[0_0_24px_rgba(93,230,255,0.4)] hover:shadow-[0_0_35px_rgba(93,230,255,0.6)] transition-all">
      <span class="material-symbols-outlined text-[18px]">home</span>
      Return Home
    </a>
    <a href="services.html" class="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-surface-container hover:bg-surface-container-high text-on-surface border border-outline-variant/30 transition-all">
      <span class="material-symbols-outlined text-[18px] text-secondary">explore</span>
      Explore All Services
    </a>
  </div>
</section>
"""
    header = render_header('404')
    footer = render_footer()
    mobile = render_mobile_bar()
    full = f"""<!DOCTYPE html>
<html class="dark scroll-smooth" lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 — Page Not Found | Zyntara AI Systems</title>
  {FAVICON_SVG}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
  {TAILWIND_CONFIG_SCRIPT}
</head>
<body class="bg-background font-body-md text-on-surface antialiased min-h-screen flex flex-col">
  {header}
  <main class="w-full pt-20 bg-background flex-1 pb-24 md:pb-0">{content}</main>
  {mobile}
  {footer}
  {SHARED_SCRIPTS}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, '404.html'), 'w') as f:
        f.write(full)
    print("Generated 404.html")

build_privacy_page()
build_terms_page()
build_404_page()

# Sync everything to public/ directory for Render / production static hosting
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')
os.makedirs(PUBLIC_DIR, exist_ok=True)
for item in os.listdir(BASE_DIR):
    if item.endswith('.html') or item == 'assets' or item == 'docs':
        src_p = os.path.join(BASE_DIR, item)
        dst_p = os.path.join(PUBLIC_DIR, item)
        if os.path.isdir(src_p):
            shutil.copytree(src_p, dst_p, dirs_exist_ok=True)
        else:
            shutil.copy2(src_p, dst_p)

print("All pages successfully built and synced to public/!")
