
import streamlit as st
from collections import Counter
import re

# إعداد الصفحة
st.set_page_config(
    page_title="Pocket AI Analyzer",
    page_icon="📊",
    layout="wide"
)

# تصميم التطبيق
st.title("📊 Pocket AI Analyzer")
st.subheader("المحلل التعليمي للرسوم البيانية")
st.write("ارفع صورة الرسم البياني للحصول على شرح تعليمي للعناصر الظاهرة.")

st.divider()

# القائمة الجانبية
st.sidebar.title("⚙️ القائمة الرئيسية")

page = st.sidebar.radio(
    "اختر القسم:",
    [
        "تحليل الصور",
        "تحليل النصوص",
        "شرح المؤشرات",
        "حول التطبيق"
    ]
)

# قسم تحليل الصور
if page == "تحليل الصور":

    st.header("🖼️ رفع صورة الرسم البياني")

    uploaded_image = st.file_uploader(
        "اختر صورة:",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image is not None:

        st.image(
            uploaded_image,
            caption="الرسم البياني المرفوع",
            use_container_width=True
        )

        st.success("تم رفع الصورة بنجاح!")

        st.divider()

        st.header("📈 عناصر التحليل التعليمي")

        st.subheader("1️⃣ مؤشر RSI")
        st.write(
            "يُستخدم مؤشر RSI لدراسة زخم الحركة "
            "ومعرفة ما إذا كان المؤشر في مناطق مرتفعة أو منخفضة."
        )

        st.subheader("2️⃣ مؤشر MACD")
        st.write(
            "يساعد MACD على دراسة الزخم "
            "والتقاطع بين خطوط المؤشر."
        )

        st.subheader("3️⃣ المتوسطات المتحركة")
        st.write(
            "تساعد المتوسطات المتحركة على فهم "
            "الاتجاه العام للحركة السعرية."
        )

        st.subheader("4️⃣ الشموع اليابانية")
        st.write(
            "يمكن دراسة أجسام الشموع والظلال "
            "والأنماط المختلفة لفهم حركة السعر."
        )

        st.subheader("5️⃣ الدعم والمقاومة")
        st.write(
            "مناطق سعرية تعليمية تساعد على دراسة "
            "المستويات التي ظهر عندها تغير في الحركة."
        )

        st.subheader("6️⃣ الاتجاه العام")

        direction = st.selectbox(
            "اختر الاتجاه الذي تلاحظه في الرسم:",
            [
                "غير محدد",
                "اتجاه صاعد",
                "اتجاه هابط",
                "اتجاه جانبي"
            ]
        )

        st.write("الاتجاه المختار:", direction)

        st.divider()

        st.header("📝 التقرير التعليمي")

        st.info(
            "تم رفع الصورة. الأقسام السابقة تشرح المؤشرات "
            "التي يمكنك دراستها في الرسم البياني. "
            "هذا الإصدار لا يستخرج قراءات المؤشرات تلقائياً "
            "من الصورة ولا يقدم توصيات تداول."
        )

# قسم تحليل النصوص
elif page == "تحليل النصوص":

    st.header("📝 تحليل النصوص")

    text = st.text_area("اكتب النص هنا:")

    if st.button("تحليل النص"):

        if text.strip():

            words = re.findall(
                r"\b\w+\b",
                text.lower()
            )

            st.subheader("نتائج التحليل")

            st.write("عدد الأحرف:", len(text))
            st.write("عدد الكلمات:", len(words))
            st.write("الكلمات الفريدة:", len(set(words)))

            common = Counter(words).most_common(5)

            st.subheader("أكثر الكلمات تكراراً")

            for word, count in common:
                st.write(f"{word}: {count}")

        else:
            st.warning("يرجى كتابة نص أولاً.")

# قسم شرح المؤشرات
elif page == "شرح المؤشرات":

    st.header("📚 مكتبة المؤشرات التعليمية")

    with st.expander("RSI"):
        st.write(
            "مؤشر القوة النسبية، ويستخدم لدراسة زخم السعر."
        )

    with st.expander("MACD"):
        st.write(
            "مؤشر يساعد على دراسة الزخم والتغيرات في الاتجاه."
        )

    with st.expander("Moving Average"):
        st.write(
            "المتوسط المتحرك يساعد على تنعيم حركة السعر."
        )

    with st.expander("Candlesticks"):
        st.write(
            "الشموع اليابانية تعرض معلومات عن الافتتاح "
            "والإغلاق وأعلى وأدنى سعر."
        )

    with st.expander("Support & Resistance"):
        st.write(
            "الدعم والمقاومة مفهومان لدراسة مستويات السعر."
        )

# حول التطبيق
elif page == "حول التطبيق":

    st.header("ℹ️ حول Pocket AI Analyzer")

    st.write(
        "مشروع تعليمي لدراسة النصوص والرسوم البيانية "
        "وفهم المؤشرات الفنية."
    )

    st.warning(
        "التطبيق لا يقدم إشارات شراء أو بيع، "
        "ولا يتنبأ بنتائج الصفقات."
    )

# أسفل الصفحة
st.divider()

st.caption(
    "Pocket AI Analyzer | Educational Project"
)
