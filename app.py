
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Pocket AI Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Pocket AI Analyzer")
st.caption("أداة تعليمية لفهم الرسوم البيانية وقياس دقة التصنيف التاريخي")

st.info(
    "هذه الأداة تعليمية. لا تقدم إشارات شراء أو بيع، "
    "ولا تتنبأ بنتائج الصفقات."
)

st.header("🖼️ تحليل الرسم البياني")

image_file = st.file_uploader(
    "ارفع صورة الرسم البياني",
    type=["png", "jpg", "jpeg"]
)

if image_file:
    st.image(
        image_file,
        caption="الرسم البياني المرفوع",
        use_container_width=True
    )

    st.subheader("وصف الرسم البياني")

    st.write(
        "تم تحميل الصورة بنجاح. يمكن استخدام هذا القسم "
        "لتسجيل ملاحظات تعليمية عن الشموع والاتجاه والمؤشرات."
    )

    direction = st.selectbox(
        "ما الاتجاه الذي تلاحظه في الرسم؟",
        ["غير محدد", "صاعد", "هابط", "جانبي"]
    )

    st.write("الاتجاه الذي اخترته:", direction)

st.divider()

st.header("📈 المؤشرات الفنية")

indicator = st.selectbox(
    "اختر المؤشر الذي تريد معرفة المزيد عنه",
    ["RSI", "MACD", "المتوسطات المتحركة", "الشموع اليابانية"]
)

explanations = {
    "RSI": "مؤشر RSI يقيس زخم حركة السعر، ويتراوح عادة بين 0 و100.",
    "MACD": "مؤشر MACD يساعد على دراسة الزخم والعلاقة بين متوسطات السعر.",
    "المتوسطات المتحركة": "تساعد على تلخيص حركة السعر خلال فترات زمنية مختلفة.",
    "الشموع اليابانية": "تعرض الشموع أسعار الافتتاح والإغلاق وأعلى وأدنى سعر."
}

st.info(explanations[indicator])

st.divider()

st.header("🧪 اختبار الدقة التاريخية")

st.write(
    "ارفع بيانات تاريخية بصيغة CSV تحتوي على نتائج تصنيف سابقة "
    "وقيم التصنيف الفعلية، لقياس دقة النموذج."
)

data_file = st.file_uploader(
    "اختر ملف بيانات الاختبار CSV",
    type=["csv"],
    key="historical_csv"
)

if data_file:
    try:
        data = pd.read_csv(data_file)

        st.write("معاينة البيانات:")
        st.dataframe(data.head())

        required_columns = ["actual", "predicted"]

        if all(col in data.columns for col in required_columns):
            valid = data.dropna(subset=required_columns)

            if len(valid) > 0:
                accuracy = (
                    valid["actual"].astype(str).str.strip()
                    == valid["predicted"].astype(str).str.strip()
                ).mean() * 100

                st.metric(
                    "دقة التصنيف في بيانات الاختبار",
                    f"{accuracy:.2f}%"
                )

                st.caption(
                    "هذه نتيجة اختبار على البيانات المرفوعة، "
                    "وليست احتمال نجاح صفقة مستقبلية."
                )
            else:
                st.warning("لا توجد بيانات صالحة للاختبار.")
        else:
            st.warning(
                "يجب أن يحتوي الملف على عمودين: "
                "actual و predicted."
            )

    except Exception as error:
        st.error(f"تعذر قراءة الملف: {error}")

st.divider()

st.header("ℹ️ حول التطبيق")

st.write(
    "Pocket AI Analyzer مشروع تعليمي يساعد على فهم الرسوم البيانية "
    "والمؤشرات الفنية وقياس أداء التصنيف على بيانات تاريخية."
)

st.caption("الإصدار 2.0")
