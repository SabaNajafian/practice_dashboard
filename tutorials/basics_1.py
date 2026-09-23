#imports 
import streamlit as st
import pandas as pd
import numpy as np

#this is my practice version of the streamlit doc (it is one of the best docs i have read so far )
# https://docs.streamlit.io/get-started/fundamentals/main-concepts#use-magic

st.markdown('# some basics')
st.markdown('## magic')
st.markdown('**first thing that you have to learn** is that streamlit is going to wrap everything in the write function')

#everything you write is going to be wrapped around by a write method by default
st.markdown('### without the write function:')

st.code('''#the actual code:
    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]})

df''')

#the result
st.markdown('output:')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

#now with the write wrapping 
st.markdown('### with the write function:')
st.code('''
#the actual code:
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
''')


st.write("output:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.markdown('## style it')
st.write('lets first create a random number dataframe and pose it as a table')
df = np.random.randn(10,20)
st.dataframe(df)

st.write('''
now lets try to style and highlight some items using dataframe.style built in for pandas
''')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

#try to create a code that will both show the code and the output


st.markdown('## charts')
st.code('''
#first create the data and specify the columns 
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    
#then use the line_chart to draw it
st.line_chart(chart_data)
''')

st.write('outputs:')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)



st.markdown('## maps')
st.code('''
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
        ''')

st.write('outputs:')
np.random.seed(42)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


st.markdown('## widgets ')
st.write('this is code will be interactive so whenever you toggle it, all the code is going to be read from top to bottom')

st.markdown('### slider')
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.markdown('### text input')


st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name



st.markdown('## check box')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data
    
    

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
    df['first column'].index)

'You selected: ', option
df
df.loc[option , 'first column']

'without the write function i can just write freely here'


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
    
