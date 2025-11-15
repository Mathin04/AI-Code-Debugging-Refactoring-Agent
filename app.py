import streamlit as st
from agent import code_debugger_agent

st.title('AI Code Debugging & Refactoring Agent')

st.sidebar.header('Options')
filename_hint = st.sidebar.text_input('Filename hint')
run_tests = st.sidebar.checkbox('Run tests', value=True)

code = st.text_area('Paste code here', height=300)

if st.button('Analyze'):
    if not code.strip():
        st.warning('Please paste some code')
    else:
        with st.spinner('Analyzing...'):
            result = code_debugger_agent(code, filename_hint=filename_hint, run_tests=run_tests)

        st.subheader('Language')
        st.code(result.language)

        st.subheader('Errors')
        if result.errors:
            for e in result.errors:
                st.error(e)
        else:
            st.success('No syntax issues')

        st.subheader('Suggestions')
        for s in result.suggestions:
            st.write('- ' + s)

        st.subheader('Optimized Code')
        st.code(result.optimized_code)

        st.subheader('Test Output')
        st.text(result.test_output)
