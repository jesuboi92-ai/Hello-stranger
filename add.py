import streamlit as st
import random
import time

# --- ASETUKSET ---
st.set_page_config(page_title="Hello Stranger", page_icon="👋", layout="centered")

# --- KIELET / SANASTO ---
translations = {
    "FI": {
        "title": "HELLO STRANGER",
        "profile_settings": "⚙️ Oma Profiili & Asetukset",
        "matches": "💬 Omat Matchit & Chatit",
        "extra_title": "HELLO STRANGER EXTRA",
        "credits": "Krediitit",
        "extra_btn": "🌟 Extra & Ominaisuudet",
        "filters": "⚙️ Hakusuodattimet",
        "city": "Kaupunki / Sijainti",
        "age_range": "Ikähaarukka",
        "hobby": "Harrastus / Kiinnostuksen kohde",
        "distance": "Etäisyys (km)",
        "logout": "🚪 Kirjaudu ulos",
        "save": "💾 Tallenna muutokset",
        "name": "Nimi",
        "age": "Ikä",
        "loc": "Kaupunki",
        "gender": "Oma sukupuoli",
        "seeking": "Ketä etsit?",
        "hobbies": "Harrastukset",
        "bio": "Bio / Esittely",
        "language": "Kieli / Language",
        "images_title": "Omat profiilikuvat (1–6 kpl)",
        "image_url_placeholder": "Kuvan URL-osoite",
        "live_warning": "⚠️ Ei vahvistettu",
        "live_ok": "📸 Vahvistettu",
        "preview_title": "Oman profiilin esikatselu",
        "image_label": "Kuva",
        "extra_desc": "Hienostunut lista ominaisuuksia:",
        "undo_feature": "• Undo Hello (Peru Hellot)",
        "comp_feature": "• Advanced Compatibility Data (Syvemmät Match Quality -tiedot)",
        "boost_feature": "• Profile Boost (Parannettu näkyvyys)",
        "ads_feature": "• No Ads (Ei mainoksia)",
        "price_tag": "• Hinta (esim. $4.99/kk) ja 'UPGRADE NOW' (Tilaa nyt) -painike ruusukulta-mustateemalla.",
        "upgrade_now": "UPGRADE NOW"
    },
    "EN": {
        "title": "HELLO STRANGER",
        "profile_settings": "⚙️ My Profile & Settings",
        "matches": "💬 My Matches & Chats",
        "extra_title": "HELLO STRANGER EXTRA",
        "credits": "Credits",
        "extra_btn": "🌟 Extra & Features",
        "filters": "⚙️ Search Filters",
        "city": "City / Location",
        "age_range": "Age Range",
        "hobby": "Hobby / Interest",
        "distance": "Distance (km)",
        "logout": "🚪 Log out",
        "save": "💾 Save Changes",
        "name": "Name",
        "age": "Age",
        "loc": "City",
        "gender": "My Gender",
        "seeking": "Who are you looking for?",
        "hobbies": "Hobbies",
        "bio": "Bio",
        "language": "Language / Kieli",
        "images_title": "Profile Pictures (1–6 pcs)",
        "image_url_placeholder": "Image URL",
        "live_warning": "⚠️ Not Verified",
        "live_ok": "📸 Verified",
        "preview_title": "My Profile Preview",
        "image_label": "Picture",
        "extra_desc": "A sophisticated list of features:",
        "undo_feature": "• Undo Hellos",
        "comp_feature": "• Advanced Compatibility Data (Deeper Match Quality Insights)",
        "boost_feature": "• Profile Boost (Enhanced Visibility)",
        "ads_feature": "• No Ads",
        "price_tag": "• Price (e.g. $4.99/mo) and 'UPGRADE NOW' button in rose gold-black theme.",
        "upgrade_now": "UPGRADE NOW"
    }
}

# --- TILANHALLINTA ---
if 'app_stage' not in st.session_state:
    st.session_state.app_stage = 'onboarding'
if 'profile_idx' not in st.session_state:
    st.session_state.profile_idx = 0
if 'credits' not in st.session_state:
    st.session_state.credits = 3
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'matches' not in st.session_state:
    st.session_state.matches = []
if 'liked_profile_ids' not in st.session_state:
    st.session_state.liked_profile_ids = set()
if 'lang' not in st.session_state:
    st.session_state.lang = 'FI'

t = translations[st.session_state.lang]

if 'my_profile' not in st.session_state:
    st.session_state.my_profile = {
        "email": "", "name": "Jesse", "age": 28, "loc": "Turku",
        "gender": "Mies", "seeking": ["Naiset"],
        "hobbies": ["Koodaus", "Kahvi", "Matkustus"],
        "bio": "Kahvia, koodia ja matkustelua ☕",
        "images": [
            "https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
        ],
        "verified": False
    }

if st.session_state.logged_in and st.session_state.app_stage == 'onboarding':
    st.session_state.app_stage = 'discover'

# --- VAKIOT JA POOLIT ---
all_hobbies_pool = ["Matkustus", "Kahvi", "Koodaus", "Kokkaus", "Taide", "Valokuvaus", "Musiikki", "Luonto", "Kuntosali", "Kirjoittaminen", "Cocktailit", "Ulkoilu"]
cities = ["Helsinki", "Turku", "Tampere", "Oulu", "Jyväskylä", "Lahti"]

name_pool_women = ["Jenna", "Sofia", "Emilia", "Laura", "Hanna", "Sara", "Maria", "Elina", "Johanna", "Kaisa"]
name_pool_men = ["Lukas", "Elias", "Aleksi", "Mikael", "Jesse", "Joonas", "Oskari", "Henri", "Santeri", "Ville"]

img_pool_women = [
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
]

img_pool_men = [
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
]

if 'all_profiles' not in st.session_state:
    st.session_state.all_profiles = []

def generate_more_profiles(count=5):
    for i in range(count):
        gender = random.choice(["Nainen", "Mies"])
        if gender == "Nainen":
            name = random.choice(name_pool_women)
            img = random.choice(img_pool_women)
        else:
            name = random.choice(name_pool_men)
            img = random.choice(img_pool_men)
            
        new_p = {
            "id": f"gen_{random.randint(10000, 99999)}",
            "name": name,
            "age": random.randint(20, 38),
            "loc": random.choice(cities),
            "gender": gender,
            "hobbies": random.sample(all_hobbies_pool, 3),
            "match_pct": random.randint(70, 99),
            "img": img,
            "bio": "Etsin seuraa hyviin keskusteluihin ja spontaaneille reissuille ☕✨",
            "verified": random.choice([True, False]),
            "custom_opening": "Hei! Kiva match! 😊"
        }
        st.session_state.all_profiles.append(new_p)

if len(st.session_state.all_profiles) < 5:
    generate_more_profiles(10)

# --- TYYLIT ---
st.markdown("""
    <style>
    .stApp { background-color: #0c0c0c; color: #f0f0f0; }
    .rose-gold-text { color: #c58b76; text-align: center; font-weight: 700; letter-spacing: 1px; }
    .discover-card {
        position: relative; background: rgba(22, 22, 22, 0.85); backdrop-filter: blur(16px);
        border-radius: 24px; overflow: hidden; border: 1px solid rgba(197, 139, 118, 0.25);
        box-shadow: 0 16px 40px rgba(0,0,0,0.7); margin-bottom: 20px;
    }
    div.stButton > button {
        border-radius: 24px; height: 48px; font-weight: 700;
        border: 1px solid rgba(255,255,255,0.1); background-color: #1a1a1a; color: white;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover { border-color: #c58b76; }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #d4af37 0%, #c58b76 100%);
        border: none; color: #121212;
    }
    div[data-testid="stChatInput"] textarea { color: #000000 !important; }
    div[data-testid="stChatInput"] { background-color: #f0f0f0 !important; border-radius: 12px; }
    </style>
""", unsafe_allow_html=True)

# --- SIVUPALKKI ---
age_range = (18, 65)

if st.session_state.app_stage not in ['onboarding']:
    with st.sidebar:
        avatar_img = st.session_state.my_profile['images'][0] if st.session_state.my_profile['images'] else "https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <img src="{avatar_img}" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; border: 2px solid #c58b76;">
            <div>
                <div style="font-weight: 700; font-size: 1.1em; color: #fff;">{st.session_state.my_profile['name']}</div>
                <div style="font-size: 0.8em; color: #888;">{st.session_state.my_profile['loc']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.my_profile['verified']:
            st.success(t["live_ok"])
        else:
            st.warning(t["live_warning"])
        
        if st.button(t["profile_settings"], use_container_width=True, key="sb_profile"):
            st.session_state.app_stage = 'profile_settings'
            st.rerun()
            
        if st.button(t["matches"], use_container_width=True, key="sb_matches"):
            st.session_state.app_stage = 'matches_list'
            st.rerun()
            
        st.markdown("---")
        st.markdown(f"<h3 class='rose-gold-text'>{t['extra_title']}</h3>", unsafe_allow_html=True)
        st.info(f"💎 {t['credits']}: {st.session_state.credits} kpl")
        if st.button(t["extra_btn"], use_container_width=True, type="primary", key="sb_extra"):
            st.session_state.app_stage = 'extra'
            st.rerun()
            
        st.markdown("---")
        st.subheader(t["filters"])
        st.selectbox(t["city"], ["Kaikki kaupungit", "Helsinki", "Turku", "Tampere", "Oulu"], key="sb_city")
        age_range = st.slider(t["age_range"], 18, 65, (18, 65), key="sb_age")
        st.session_state['filter_hobby'] = st.selectbox(t["hobby"], ["Kaikki", "Matkustus", "Kahvi", "Koodaus"], key="sb_hobby")

        if st.button(t["logout"], use_container_width=True, key="sb_logout"):
            st.session_state.logged_in = False
            st.session_state.app_stage = 'onboarding'
            st.rerun()

# --- SUODATUS & AUTOMAATTINEN LISÄYS ---
seeking_prefs = st.session_state.my_profile['seeking']
user_hobby_filter = st.session_state.get('filter_hobby', "Kaikki")

filtered_profiles = []
for p in st.session_state.all_profiles:
    if p['id'] in st.session_state.liked_profile_ids:
        continue
    gender_match = ("Naiset" in seeking_prefs and p['gender'] == "Nainen") or ("Miehet" in seeking_prefs and p['gender'] == "Mies")
    if gender_match and age_range[0] <= p['age'] <= age_range[1]:
        if user_hobby_filter == "Kaikki" or user_hobby_filter in p.get('hobbies', []):
            filtered_profiles.append(p)

if not filtered_profiles:
    generate_more_profiles(5)
    st.rerun()

current_p = filtered_profiles[st.session_state.profile_idx % len(filtered_profiles)] if filtered_profiles else None

# --- 1. ONBOARDING ---
if st.session_state.app_stage == 'onboarding':
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='rose-gold-text' style='font-size: 3em;'>{t['title']} 👋</h1>", unsafe_allow_html=True)
    email = st.text_input("Sähköposti", placeholder="esim. nimi@osoite.fi", key="onb_email")
    password = st.text_input("Salasana", type="password", placeholder="••••••••", key="onb_pass")
    if st.button("🚀 KIRJAUDU / ASTU SISÄÄN", use_container_width=True, type="primary", key="onb_btn"):
        if email and password:
            st.session_state.my_profile['email'] = email
            st.session_state.logged_in = True
            st.session_state.app_stage = 'discover'
            st.rerun()

# --- 2. OMA PROFIILI & ASETUKSET ---
elif st.session_state.app_stage == 'profile_settings':
    if st.button("←", key="back_from_profile"):
        st.session_state.app_stage = 'discover'
        st.rerun()
    
    st.markdown(f"<h3 class='rose-gold-text'>{t['profile_settings']}</h3>", unsafe_allow_html=True)
    
    col_form, col_preview = st.columns([2, 1])
    
    with col_form:
        new_lang = st.selectbox(t["language"], ["FI", "EN"], index=["FI", "EN"].index(st.session_state.lang), key="lang_selector")
        if new_lang != st.session_state.lang:
            st.session_state.lang = new_lang
            st.rerun()

        p_name = st.text_input(t["name"], st.session_state.my_profile['name'], key="p_set_name")
        p_age = st.number_input(t["age"], 18, 99, st.session_state.my_profile['age'], key="p_set_age")
        p_loc = st.text_input(t["loc"], st.session_state.my_profile['loc'], key="p_set_loc")
        p_gender = st.selectbox(t["gender"], ["Mies", "Nainen", "Muu"], index=["Mies", "Nainen", "Muu"].index(st.session_state.my_profile['gender']), key="p_set_gender")
        p_seeking = st.multiselect(t["seeking"], ["Naiset", "Miehet", "Muut"], default=st.session_state.my_profile['seeking'], key="p_set_seeking")
        p_hobbies = st.multiselect(t["hobbies"], all_hobbies_pool, default=st.session_state.my_profile.get('hobbies', ["Koodaus"]), key="p_set_hobbies")
        p_bio = st.text_area(t["bio"], st.session_state.my_profile['bio'], key="p_set_bio")
        
        st.markdown(f"**{t['images_title']}**")
        current_images = st.session_state.my_profile.get('images', [])
        updated_images = []
        for i in range(6):
            default_val = current_images[i] if i < len(current_images) else ""
            img_input = st.text_input(f"{t['image_label']} {i+1}", value=default_val, placeholder=t["image_url_placeholder"], key=f"user_img_{i}")
            if img_input.strip():
                updated_images.append(img_input.strip())

    with col_preview:
        st.markdown(f"##### {t['preview_title']}")
        preview_img = updated_images[0] if updated_images else "https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
        st.markdown(f"""
        <div style="background: #161616; border-radius: 16px; padding: 12px; border: 1px solid rgba(197,139,118,0.3); text-align: center;">
            <img src="{preview_img}" style="width: 100%; height: 220px; border-radius: 12px; object-fit: cover;">
            <h4 style="margin: 10px 0 2px 0;">{p_name}, {p_age}</h4>
            <p style="color: #888; font-size: 0.85em; margin: 0;">{p_loc}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button(t["save"], use_container_width=True, type="primary", key="p_set_save"):
        st.session_state.my_profile.update({
            "name": p_name, "age": p_age, "loc": p_loc, "gender": p_gender, 
            "seeking": p_seeking, "hobbies": p_hobbies, "bio": p_bio, "images": updated_images
        })
        st.session_state.app_stage = 'discover'
        st.rerun()

# --- 3. EXTRA (Päivitetty vastaamaan tarkasti annettua kuvaa) ---
elif st.session_state.app_stage == 'extra':
    if st.button("←", key="back_from_extra"):
        st.session_state.app_stage = 'discover'
        st.rerun()
        
    st.markdown(f"<h2 class='rose-gold-text'>{t['extra_title']}</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: rgba(22, 22, 22, 0.9); border: 1px solid rgba(197, 139, 118, 0.4); border-radius: 20px; padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.8);">
        <p style="color: #c58b76; font-weight: 700; font-size: 1.1em; margin-bottom: 12px;">{t['extra_desc']}</p>
        <ul style="color: #e0e0e0; line-height: 1.8; font-size: 1.05em; list-style-type: none; padding-left: 0;">
            <li>{t['undo_feature']}</li>
            <li>{t['comp_feature']}</li>
            <li>{t['boost_feature']}</li>
            <li>{t['ads_feature']}</li>
        </ul>
        <hr style="border-color: rgba(197, 139, 118, 0.2); margin: 20px 0;">
        <p style="color: #aaa; font-size: 0.95em; text-align: center;">{t['price_tag']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(t["upgrade_now"], use_container_width=True, type="primary", key="upgrade_btn"):
        st.session_state.credits += 15
        st.success("Tilaus aktivoitu! +15 krediittiä lisätty tilillesi 🌟")
        st.rerun()

# --- 4. DISCOVER ---
elif st.session_state.app_stage == 'discover':
    st.markdown(f"<h3 class='rose-gold-text' style='margin:0;'>{t['title']} 👋</h3>", unsafe_allow_html=True)

    if current_p:
        hobbies_badges = " ".join([f"<span style='background:rgba(197,139,118,0.15); color:#c58b76; padding:4px 10px; border-radius:12px; font-size:0.8em; font-weight:600; margin-right:6px;'>#{h}</span>" for h in current_p.get('hobbies', [])])
        
        verified_badge = " ✔️ <span style='color: #4CAF50; font-size: 0.75em;'>Vahvistettu</span>" if current_p.get('verified') else " ❌ <span style='color: #f44336; font-size: 0.75em;'>Ei vahvistettu</span>"
        if st.session_state.lang == 'EN':
            verified_badge = " ✔️ <span style='color: #4CAF50; font-size: 0.75em;'>Verified</span>" if current_p.get('verified') else " ❌ <span style='color: #f44336; font-size: 0.75em;'>Not Verified</span>"

        st.markdown(f"""
        <div class="discover-card">
            <div style="width: 100%; height: 420px; background-color: #000000; display: flex; justify-content: center; align-items: center; overflow: hidden;">
                <img src="{current_p['img']}" style="width: 100%; height: 100%; object-fit: contain; object-position: center;">
            </div>
            <div style="padding: 20px; background: linear-gradient(to top, #161616 85%, transparent);">
                <h2 style="margin: 0 0 4px 0; font-size: 1.6em;">{current_p['name']}, {current_p['age']} {verified_badge} <span style="font-size: 0.7em; color: #888;">· {current_p['loc']}</span></h2>
                <p style="margin: 8px 0 12px 0;">{hobbies_badges}</p>
                <p style="color: #ccc; font-size: 0.95em; margin-bottom: 0;">{current_p['bio']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("❌ DISMISS", use_container_width=True, key="disc_dismiss"):
                st.session_state.liked_profile_ids.add(current_p['id'])
                st.session_state.profile_idx += 1
                st.rerun()
        with col2:
            if st.button("👋 SAY HELLO", use_container_width=True, type="primary", key="disc_hello"):
                st.session_state.liked_profile_ids.add(current_p['id'])
                st.session_state.active_chat_target = current_p
                st.session_state.app_stage = 'match_success'
                st.rerun()
        with col3:
            if st.button("💬 HELLO + VIESTI", use_container_width=True, key="disc_msg"):
                st.session_state.liked_profile_ids.add(current_p['id'])
                st.session_state.active_chat_target = current_p
                st.session_state.app_stage = 'chat'
                st.rerun()

# --- 5. MATCH SUCCESS ---
elif st.session_state.app_stage == 'match_success':
    target = st.session_state.get('active_chat_target', current_p)
    my_img = st.session_state.my_profile['images'][0] if st.session_state.my_profile['images'] else "https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    
    st.markdown(f"<h1 class='rose-gold-text' style='font-size: 2.5em; margin: 20px 0; text-align: center;'>IT'S A MATCH!</h1>", unsafe_allow_html=True)
    
    col_img1, col_heart, col_img2 = st.columns([3, 1, 3])
    with col_img1:
        st.markdown(f"""<div style="display: flex; justify-content: center;"><img src="{my_img}" style="width: 140px; height: 140px; border-radius: 50%; object-fit: cover; border: 3px solid #c58b76;"></div>""", unsafe_allow_html=True)
    with col_heart:
        st.markdown("<h2 style='text-align: center; color: #c58b76; line-height: 140px; margin: 0;'>💖</h2>", unsafe_allow_html=True)
    with col_img2:
        st.markdown(f"""<div style="display: flex; justify-content: center;"><img src="{target['img']}" style="width: 140px; height: 140px; border-radius: 50%; object-fit: cover; border: 3px solid #c58b76;"></div>""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💬 JATKA CHATTIIN", use_container_width=True, type="primary", key="match_chat_btn"):
        if target not in st.session_state.matches:
            st.session_state.matches.append(target)
        st.session_state.app_stage = 'chat'
        st.rerun()

# --- 6. CHAT ---
elif st.session_state.app_stage == 'chat':
    if st.button("←", key="back_from_chat"):
        st.session_state.app_stage = 'discover'
        st.rerun()
        
    target = st.session_state.get('active_chat_target', None)
    if target:
        st.markdown(f"### 💬 {target['name']}, {target['age']}")
        st.markdown("---")
        
        chat_key = f"messages_{target['id']}"
        if chat_key not in st.session_state:
            st.session_state[chat_key] = [{"role": "assistant", "content": target['custom_opening']}]
            
        for msg in st.session_state[chat_key]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                
        user_input = st.chat_input("Kirjoita viesti...", key=f"chat_input_{target['id']}")
        if user_input:
            st.session_state[chat_key].append({"role": "user", "content": user_input})
            st.session_state[chat_key].append({"role": "assistant", "content": "Ihana kuulla! Mites sun viikonloppu muuten sujuu? 😊"})
            st.rerun()
