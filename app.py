
import streamlit as st
import pandas as pd
import html

from pumping_lemma import (
    check_language,
    generate_strings,
    generate_splits,
    pump_string,
    verify_conditions
)

st.set_page_config(
    page_title="Pumping Lemma Demonstrator",
    page_icon="📘",
    layout="wide"
)

st.title("Pumping Lemma for Regular Languages")
st.write("Interactive visualization of the Pumping Lemma using Python.")

st.divider()

# 1. Select language
st.subheader("1. Select Language")

language = st.selectbox(
    "Choose a language",
    ["a*b*", "a^n b^n"]
)

if language == "a*b*":
    st.latex(r"L = \{a^m b^n \mid m,n \geq 0\}")
else:
    st.latex(r"L = \{a^n b^n \mid n \geq 0\}")

# 2. Pumping length
st.subheader("2. Enter Pumping Length")

p = st.number_input(
    "Pumping length (p)",
    min_value=1,
    max_value=20,
    value=3,
    step=1
)

# 3. Generate strings
st.subheader("3. Generate Candidate Strings")

if st.button("Generate Strings"):
    st.session_state.candidates = generate_strings(
        language, int(p)
    )

if "candidates" in st.session_state:

    candidates = st.session_state.candidates

    if candidates:

        st.success("Candidate strings generated successfully!")

        st.write(", ".join(
            word if word else "ε" for word in candidates
        ))

        # 4. Select string
        st.subheader("4. Select a String")

        word = st.selectbox(
            "Choose candidate string",
            candidates,
            format_func=lambda w: w if w else "ε"
        )

        st.write("Selected string:", word if word else "ε")

        # 5. Generate splits
        splits = generate_splits(word, int(p))

        st.subheader("5. Select a Valid Split")

        if splits:

            split_labels = [
                f"x={x or 'ε'}, y={y}, z={z or 'ε'}"
                for x, y, z in splits
            ]

            selected = st.selectbox(
                "Choose decomposition",
                range(len(splits)),
                format_func=lambda index: split_labels[index]
            )

            x, y, z = splits[selected]

            # VISUALIZATION 1: X-Y-Z decomposition
            st.subheader("Visualization 1: String Decomposition")

            st.write("The selected string is divided into x, y and z.")

            x_display = html.escape(x) if x else "ε"
            y_display = html.escape(y)
            z_display = html.escape(z) if z else "ε"

            st.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    gap:8px;
                    flex-wrap:wrap;
                    padding:20px;
                    font-size:24px;
                    font-weight:bold;
                ">
                    <div style="background:#DCEBFF;color:#1455A0;
                    padding:15px 22px;border-radius:10px;">
                        x = {x_display}
                    </div>
                    <div style="background:#FFE3A8;color:#855000;
                    padding:15px 22px;border-radius:10px;">
                        y = {y_display}
                    </div>
                    <div style="background:#D8F5DF;color:#176B35;
                    padding:15px 22px;border-radius:10px;">
                        z = {z_display}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                "Blue = x | Yellow = y (repeated part) | Green = z"
            )

            st.latex(r"w = xyz")

            # Check pumping conditions
            st.subheader("6. Verify Pumping Conditions")

            conditions = verify_conditions(
                word, x, y, z, int(p), language
            )

            for condition, result in conditions.items():
                if result:
                    st.success("✓ " + condition)
                else:
                    st.error("✗ " + condition)

            # 7. Enter i values
            st.subheader("7. Enter Pumping Values (i)")

            i_values = st.text_input(
                "Enter i values separated by commas",
                value="0,1,2,3,4"
            )

            if st.button("Pump and Generate Graphs"):

                try:
                    values = [
                        int(v.strip())
                        for v in i_values.split(",")
                    ]

                    if not values or any(
                        i < 0 or i > 100 for i in values
                    ):
                        st.error(
                            "Enter non-negative i values between 0 and 100."
                        )

                    elif len(set(values)) != len(values):
                        st.error("Please enter unique i values.")

                    else:

                        results = []

                        for i in values:

                            pumped = pump_string(x, y, z, i)

                            belongs = check_language(
                                pumped, language
                            )

                            results.append({
                                "i": i,
                                "Pumped String": pumped if pumped else "ε",
                                "String Length": len(pumped),
                                "Membership": (
                                    "Accepted" if belongs else "Rejected"
                                ),
                                "Accepted Value": int(belongs)
                            })

                        st.session_state.pumping_results = results

                        st.subheader("8. Pumping Results")

                        for result in results:

                            st.write(
                                f"**i = {result['i']}**"
                            )

                            st.code(
                                f"xy^{result['i']}z = "
                                f"{result['Pumped String']}"
                            )

                            if result["Membership"] == "Accepted":
                                st.success(
                                    "String belongs to the language."
                                )
                            else:
                                st.error(
                                    "String does NOT belong to the language."
                                )

                        # Prepare graph data
                        df = pd.DataFrame(results)

                        st.divider()

                        # VISUALIZATION 2: Pumping graph
                        st.subheader(
                            "Visualization 2: Pumping Graph"
                        )

                        st.write(
                            "This graph shows how the length of "
                            "the pumped string changes with i."
                        )

                        length_graph = df.set_index("i")[
                            ["String Length"]
                        ]

                        st.line_chart(length_graph)

                        st.caption(
                            "X-axis: Pumping value (i) | "
                            "Y-axis: Length of pumped string"
                        )

                        # VISUALIZATION 3: Membership graph
                        st.subheader(
                            "Visualization 3: Membership Graph"
                        )

                        st.write(
                            "Comparison of accepted and rejected "
                            "pumped strings."
                        )

                        membership_counts = (
                            df["Membership"]
                            .value_counts()
                            .reindex(
                                ["Accepted", "Rejected"],
                                fill_value=0
                            )
                        )

                        membership_graph = pd.DataFrame({
                            "Number of strings": membership_counts
                        })

                        st.bar_chart(membership_graph)

                        st.caption(
                            "Shows how many pumped strings belong "
                            "to the selected language."
                        )

                        # Detailed result table
                        st.subheader("Complete Results Table")

                        st.dataframe(
                            df[
                                [
                                    "i",
                                    "Pumped String",
                                    "String Length",
                                    "Membership"
                                ]
                            ],
                            hide_index=True,
                            use_container_width=True
                        )

                        st.info(
                            "Note: These graphs demonstrate the "
                            "selected decomposition. They do not "
                            "independently prove regularity or "
                            "non-regularity."
                        )

                except ValueError:
                    st.error(
                        "Enter valid integers separated by commas."
                    )

        else:
            st.warning("No valid decomposition found.")

    else:
        st.warning("No candidate strings were generated.")

st.divider()

st.caption(
    "FAFL Activity | Pumping Lemma Demonstration Tool"
)
