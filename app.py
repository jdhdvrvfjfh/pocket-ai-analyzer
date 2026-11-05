
import streamlit as st

st.set_page_config(
    page_title="Pocket AI Analyzer",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Pocket AI Analyzer")
st.caption("محلل تعليمي للرسوم البيانية")

st.info(
    "ارفع صورة واحدة للحصول على وصف تعليمي للرسم البياني. "
    "النتائج ليست توصيات تداول أو توقعات لنتائج الصفقات."
)

image = st.file_uploader(
    "📸 ارفع صورة الرسم البياني",
    type=["png", "jpg", "jpeg"]
)

if image:
    st.image(
        image,
        caption="الصورة المرفوعة",
        use_container_width=True
    )

    st.divider()
    st.subheader("📋 معلومات الصورة")

    st.write(f"اسم الملف: {image.name}")
    st.write(f"حجم الملف: {image.size / 1024:.1f} KB")

    st.subheader("🔍 ملاحظات التحليل")

    st.warning(
        "تم رفع الصورة بنجاح، لكن لم يتم تحليل محتواها آلياً بعد. "
        "يلزم دمج نموذج رؤية اصطناعية قبل عرض نتائج فعلية."
    )

    st.write("يمكن استخدام التحليل البصري لاحقاً للتعرف على:")
    st.write("- الشموع اليابانية.")
    st.write("- الاتجاه الظاهر.")
    st.write("- مؤشرات RSI وMACD إذا كانت ظاهرة.")
    st.write("- مستويات الدعم والمقاومة المحتملة.")

st.divider()

st.caption(
    "لا يقدم التطبيق إشارات شراء أو بيع، "
    "ولا يضمن نتائج مستقبلية."
)
