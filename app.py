
import streamlit as st
from collections import Counter
import re

# إعدادات الصفحة
st.set_page_config(
    page_title="Pocket AI Analyzer",
    page_icon="📊",
    layout="centered"
)

# العنوان الرئيسي
st.title("📊 Pocket AI Analyzer")
st.write("أداة تعليمية لتحليل النصوص والصور.")

st.divider()

# تحليل النصوص
st.header("📝 تحليل النصوص")

text = st.text_area("أدخل النص هنا:")

if st.button("تحليل النص"):
    if text.strip():
        words = re.findall(r"\b\w+\b", text.lower())

        st.subheader("📊 نتائج التحليل")
        st.write("عدد الأحرف:", len(text))
        st.write("عدد الكلمات:", len(words))
        st.write("عدد الكلمات الفريدة:", len(set(words)))

        common = Counter(words).most_common(5)

        st.subheader("🔤 أكثر الكلمات تكراراً")

        for word, count in common:
            st.write(f"{word}: {count}")

    else:
        st.warning("يرجى إدخال نص أولاً.")

st.divider()

# تحليل الصور
st.header("🖼️ تحليل الصور")

uploaded_image = st.file_uploader(
    "ارفع صورة الرسم البياني هنا:",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="الصورة المرفوعة",
        use_container_width=True
    )

    st.success("تم رفع الصورة بنجاح!")

    st.subheader("📊 التحليل التعليمي للرسم البياني")

    st.info(
        "يمكنك استخدام الصورة لدراسة الأنماط "
        "والاتجاهات الظاهرة في الرسوم البيانية."
    )

    st.write(
        "هذا التطبيق يعرض الصورة لأغراض تعليمية، "
        "ولا يقدم توصيات شراء أو بيع أو يتنبأ بالأسعار."
    )

st.divider()

st.caption("Pocket AI Analyzer | مشروع تعليمي")
