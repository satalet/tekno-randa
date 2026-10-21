import os
import streamlit as st
import plotly.express as px
from google import genai

st.set_page_config(
    page_title="مشروع التكنولوجيا - آثار التكنولوجيا",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&family=Reem+Kufi:wght@600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    .signature-badge {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 18px 24px;
        border-radius: 14px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        margin-bottom: 25px;
        border-right: 6px solid #00d2ff;
    }
    
    .signature-name {
        font-family: 'Reem Kufi', sans-serif;
        font-size: 26px;
        color: #00d2ff;
        font-weight: bold;
        letter-spacing: 0.5px;
    }
    
    .footer-signature {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        border-top: 2px dashed #00d2ff;
        font-size: 16px;
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="signature-badge">
    <div style="font-size: 14px; color: #dcdde1;">مشروع منهاج التكنولوجيا - الصف التاسع الأساسي</div>
    <div style="font-size: 22px; font-weight: bold; margin: 4px 0;">🌐 آثار التكنولوجيا في المجتمع والبيئة</div>
    <div>إعداد وتصميم الطالبة المتميزة: <span class="signature-name">رندة زربا</span> ✨</div>
</div>
""", unsafe_allow_html=True)

# استدعاء المفتاح تلقائياً من الأسرار أو من متغيرات البيئة
api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))

with st.sidebar:
    st.header("⚙️ إعدادات الذكاء الاصطناعي")
    if api_key:
        st.success("✅ تم تفعيل المفتاح تلقائياً بأمان")
    else:
        api_key = st.text_input("أدخل مفتاح Gemini API:", type="password")
    
    selected_model = st.selectbox(
        "اختر نموذج الذكاء الاصطناعي:",
        ["gemini-3.8-flash", "gemini-3.5-flash", "gemini-3.1-pro-preview"],
        index=0
    )
    st.markdown("---")
    st.markdown("**الموضوع:** آثار التكنولوجيا، النفايات الإلكترونية، والتحول الرقمي.")

tab1, tab2, tab3 = st.tabs([
    "📊 الآثار الإيجابية والسلبية", 
    "♻️ النفايات الإلكترونية (E-Waste)", 
    "🤖 اسأل الذكاء الاصطناعي"
])

with tab1:
    st.subheader("تحليل تأثير التكنولوجيا على مجالات الحياة اليومية")
    
    sectors = ["التعليم والتعلم", "الرعاية الصحية", "التواصل الاجتماعي", "البيئة والمناخ", "سوق العمل والوظائف"]
    positives = [88, 92, 75, 45, 80]
    challenges = [12, 8, 25, 55, 20]

    fig = px.bar(
        x=sectors,
        y=[positives, challenges],
        barmode='group',
        labels={'value': 'النسبة المئوية للأثر (%)', 'x': 'القطاع', 'variable': 'نوع الأثر'},
        title="مقارنة بين إيجابيات وسلبيات التكنولوجيا في مختلف القطاعات",
        color_discrete_sequence=["#00b894", "#d63031"]
    )
    fig.data[0].name = "الأثر الإيجابي"
    fig.data[1].name = "التحديات والمخاطر"
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        #### ✅ أبرز الآثار الإيجابية:
        * **التعليم:** منصات التعلم الإلكتروني وتوفير مصادر المعرفة المفتوحة للجميع.
        * **الصحة:** أجهزة التشخيص المبكر والعمليات الجراحية الدقيقة بالروبوت.
        * **الإنتاجية:** أتمتة المهام الروتينية وتسهيل الأعمال التجارية والتواصل السريع.
        """)
    with col2:
        st.error("""
        #### ⚠️ أبرز التحديات والمخاطر:
        * **الأثر الاجتماعي:** تقليل التواصل الوجاهي وظاهرة العزلة وإدمان الشاشات.
        * **الأمن الرقمي:** التهديدات السيبرانية واختراق الخصوصية الشخصية والبيانات.
        * **التحول الوظيفي:** اندثار مهن تقليدية وحاجة ماسة لتعلم مهارات تقنية جديدة.
        """)

with tab2:
    st.subheader("إدارة النفايات الإلكترونية ومخاطرها البيئية")
    st.markdown("""
    النفايات الإلكترونية هي المعدات والأجهزة الكهربائية والإلكترونية المستهلكة أو المكسورة. 
    سوء التعامل معها وحرقها العشوائي يؤدي لانبعاث غازات سامة وتسرب عناصر ضارة للمياه الجوفية والتربة.
    """)

    col_chart, col_info = st.columns([1, 1])
    
    with col_chart:
        waste_components = ["معادن ثمينة (ذهب، نحاس، فضة)", "مواد بلاستيكية", "عناصر خطرة وسامة (رصاص، زئبق)", "زجاج ومواد أخرى"]
        ratios = [35, 30, 15, 20]
        fig_waste = px.pie(
            names=waste_components,
            values=ratios,
            title="المكونات التقريبية للأجهزة الإلكترونية التالفة",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_waste, use_container_width=True)
        
    with col_info:
        st.info("""
        #### 💡 حلول عملية للتخلص الآمن:
        1. **إعادة التدوير المعتمد:** تسليم الأجهزة للشركات المتخصصة لاستخلاص المعادن بأمان.
        2. **الإصلاح وإعادة الاستخدام:** تمديد عمر الجهاز عبر الترقية والصيانة الدورية.
        3. **التوعية المدرسية:** تنظيم حملات لجمع الأجهزة المستعملة وإعادة تدويرها.
        """)

with tab3:
    st.subheader(f"اسأل المستشار الذكي (مدعوم بنموذج {selected_model})")
    st.write("اطرح أي سؤال متعلق بآثار التكنولوجيا أو منهاج الصف التاسع، وسيقوم الذكاء الاصطناعي بالإجابة فوراً وبدقة عالية.")
    
    query = st.text_input("اكتب استفسارك هنا:", placeholder="مثال: كيف أثرت التكنولوجيا سلباً وإيجاباً على مجالات التعليم؟")
    
    if st.button("إرسال الاستفسار"):
        if not api_key:
            st.warning("⚠️ المفتاح غير متوفر. يرجى إدخاله في الشريط الجانبي.")
        elif not query.strip():
            st.warning("⚠️ يرجى كتابة السؤال أولاً.")
        else:
            with st.spinner(f"جاري التحليل عبر نموذج {selected_model}..."):
                try:
                    client = genai.Client(api_key=api_key)
                    system_prompt = f"أنت معلم ومستشار تكنولوجي لمنهاج الصف التاسع الأساسي. أجب بدقة وموضوعية وبأسلوب منظم وواضح باللغة العربية الفصحى على السؤال التالي: {query}"
                    response = client.models.generate_content(
                        model=selected_model,
                        contents=system_prompt,
                    )
                    st.markdown("### 📝 الإجابة المعتمدة:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء معالجة السؤال: {e}")

st.markdown("""
<div class="footer-signature">
    تم تطوير هذه المنصة التفاعلية لدعم مادة التكنولوجيا - الصف التاسع الأساسي<br>
    بإشراف وتصميم الطالبة: <strong>رندة زربا</strong> 🌟
</div>
""", unsafe_allow_html=True)
