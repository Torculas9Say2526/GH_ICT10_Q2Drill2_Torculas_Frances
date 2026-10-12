from pyscript import display, document


def name_finder(e):
    document.getElementById('result').innerHTML = ''
    last_name = document.getElementById('surname').value.title().strip()
    first_name = document.getElementById('first').value.title().strip()
    full_name = first_name + ' ' + last_name

    cwg_members = ['Adrianna Allas', 'Jaena Ambata', 'Helena Magsino', 'Katharine Penas']

    display_message = (f'Sorry, {full_name} is not in Cosmic Writers Guild', f'{full_name} is in Cosmic Writers Guild')
    display(display_message[full_name in cwg_members], target='result')