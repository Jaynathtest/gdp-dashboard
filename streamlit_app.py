import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------------------------------------------------------
# 1) Page configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Tourism Share in GSDP Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)


# -----------------------------------------------------------------------------
# 2) Helper function to load data (cached)
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    """
    Load the CSV file 'RS Session 247 AS 7.1.csv' from the same directory as this script.
    Renames columns for convenience and drops the serial-number column.
    """
    filepath = Path(__file__).parent / "RS Session 247 AS 7.1.csv"
    df = pd.read_csv(filepath)

    # Rename columns to simpler names:
    #   'States/UTs' → 'State'
    #   'Estimated share of Tourism (Direct and Indirect) in GSDP of States/UTs (in %)' → 'Share_GSDP_pct'
    df = df.rename(
        columns={
            "States/UTs": "State",
            "Estimated share of Tourism (Direct and Indirect) in GSDP of States/UTs (in %)": "Share_GSDP_pct",
        }
    )

    # Drop the 'S. No.' column if it exists
    if "S. No." in df.columns:
        df = df.drop(columns=["S. No."])

    # Convert share column to numeric (in case it was read as string)
    df["Share_GSDP_pct"] = pd.to_numeric(df["Share_GSDP_pct"], errors="coerce")

    return df


# Load the data once (cached)
data = load_data()


# -----------------------------------------------------------------------------
# 3) Sidebar: Filters
# -----------------------------------------------------------------------------
st.sidebar.header(":mag_right: Filters")

# (a) Multiselect for states
all_states = sorted(data["State"].unique())
selected_states = st.sidebar.multiselect(
    label="Select one or more State/UT",
    options=all_states,
    default=all_states,  # by default, show all
)

# (b) If needed, you could add more filters here (e.g., by min/max share). For now, we only filter by state.

filtered = data[data["State"].isin(selected_states)]


# -----------------------------------------------------------------------------
# 4) Main Page Layout
# -----------------------------------------------------------------------------

# 4.1 Title + Description
st.title("🌐 Tourism Share in GSDP – India (State/UT-wise)")
st.markdown(
    """
This dashboard shows the **estimated share of tourism (direct + indirect)** in the GSDP of each Indian State or Union Territory.  
You can filter by State/UT in the sidebar. Hover over points in the charts to see exact values.
"""
)
st.markdown("---")


# 4.2 Top KPI Cards: Average share, Max share, Min share (across the filtered selection)
if not filtered.empty:
    avg_share = filtered["Share_GSDP_pct"].mean()
    max_row = filtered.loc[filtered["Share_GSDP_pct"].idxmax()]
    min_row = filtered.loc[filtered["Share_GSDP_pct"].idxmin()]
else:
    avg_share = max_row = min_row = None

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if avg_share is not None:
        st.metric(
            label="📊 Average Tourism Share (Filtered)",
            value=f"{avg_share:.2f}%",
        )
    else:
        st.metric(
            label="📊 Average Tourism Share (Filtered)",
            value="—",
        )

with col2:
    if max_row is not None:
        st.metric(
            label="🔝 Highest Tourism Share",
            value=f"{max_row['Share_GSDP_pct']:.2f}%",
            delta=f"{max_row['State']}",
        )
    else:
        st.metric(
            label="🔝 Highest Tourism Share",
            value="—",
        )

with col3:
    if min_row is not None:
        st.metric(
            label="🔻 Lowest Tourism Share",
            value=f"{min_row['Share_GSDP_pct']:.2f}%",
            delta=f"{min_row['State']}",
        )
    else:
        st.metric(
            label="🔻 Lowest Tourism Share",
            value="—",
        )

st.markdown("---")


# 4.3 Bar Chart: Tourism Share by State/UT
st.subheader("📈 Tourism Share in GSDP by State/UT")

if filtered.empty:
    st.warning("No data to display. Adjust your filters in the sidebar.")
else:
    # Sort by share descending
    filtered_sorted = filtered.sort_values(by="Share_GSDP_pct", ascending=False)

    # Plotly bar chart for better hover info
    import plotly.express as px

    fig_bar = px.bar(
        filtered_sorted,
        x="Share_GSDP_pct",
        y="State",
        orientation="h",
        labels={"Share_GSDP_pct": "Tourism Share (%)", "State": "State/UT"},
        text="Share_GSDP_pct",
    )
    fig_bar.update_layout(
        yaxis=dict(autorange="reversed"),  # So the highest appears on top
        margin=dict(l=120, r=20, t=30, b=40),
        height=600,
    )
    fig_bar.update_traces(texttemplate="%{text:.2f}%", textposition="outside")

    st.plotly_chart(fig_bar, use_container_width=True)


st.markdown("---")


# 4.4 Data Table: Show raw data
st.subheader("📋 Underlying Data")
st.dataframe(
    filtered.reset_index(drop=True).style.format({"Share_GSDP_pct": "{:.2f}%"}),
    height=400,
)

# 4.5 Footer / Credits
st.markdown("---")
st.markdown(
    """
<small>Data Source: `RS Session 247 AS 7.1.csv` (courtesy of user upload).</small>  
<small>Created with Streamlit.</small>
""",
    unsafe_allow_html=True,
)
