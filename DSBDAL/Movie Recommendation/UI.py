import MODEL
import tkinter as tk
import tkinter.messagebox
from functools import partial


def main_destroy():
    root.destroy()


def dummy_inputs():
    tkinter.messagebox.showinfo('Movies', 'Try this movies as Dummy Inputs:\n1. Transformers'
                                          '\n2. John Carter\n3. Gone Girl')


def get_recon_movies(user_input_dtype):
    USER_MOVIE = (user_input_dtype.get())

    recon_movies = MODEL.read_csv(USER_MOVIE)

    recon_1 = tk.Label(root, text=recon_movies[2], font=('Bahnshcrift', 12, 'bold'),
                              justify='left', bg='snow', fg='black')
    recon_1.place(x=125, y=190, width=365, height=40)

    recon_2 = tk.Label(root, text=recon_movies[3], font=('Bahnshcrift', 12, 'bold'),
                              justify='left', bg='snow', fg='black')
    recon_2.place(x=125, y=230, width=365, height=40)

    recon_3 = tk.Label(root, text=recon_movies[4], font=('Bahnshcrift', 12, 'bold'),
                              justify='left', bg='snow', fg='black')
    recon_3.place(x=125, y=270, width=365, height=40)

    recon_4 = tk.Label(root, text=recon_movies[5], font=('Bahnshcrift', 12, 'bold'),
                              justify='left', bg='snow', fg='black')
    recon_4.place(x=125, y=310, width=365, height=40)

    recon_5 = tk.Label(root, text=recon_movies[6], font=('Bahnshcrift', 12, 'bold'),
                              justify='left', bg='snow', fg='black')
    recon_5.place(x=125, y=350, width=365, height=40)


root = tk.Tk()
root.geometry("640x480+500+200")
root.title("Movie Recommendation")
root.resizable(False, False)

user_input_dtype = tk.StringVar()

background = tk.Label(root, text="", font=('Bahnshcrift', 22, 'bold'), justify='center',
                    bg='gainsboro', fg='black')
background.place(x=0, y=0, width=640, height=480)

op1_head = tk.Label(root, text="MOVIE RECOMMENDATION SYSTEM", font=('Bahnshcrift', 22, 'bold'), justify='center',
                    bg='orange', fg='black')
op1_head.place(x=0, y=0, width=670, height=70)

separator_1 = tk.Label(root, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                       bg='black', fg='black')
separator_1.place(x=0, y=0, width=670, height=3)

separator_2 = tk.Label(root, text="", font=('Bahnshcrift', 25, 'bold'), justify='center',
                       bg='black', fg='black')
separator_2.place(x=0, y=70, width=670, height=3)

# ----------------------- GET USER MOVIE -----------------------

stud_name = tk.Label(root, text="Movie", font=('Bahnshcrift', 15, 'bold'), justify='center',
                                  bg='skyblue', fg='black')
stud_name.place(x=50, y=95, width=115, height=40)

movie_name_field = tk.Entry(root, textvariable=user_input_dtype, font=('Bahnshcrift', 15, 'bold'))
movie_name_field.place(x=165, y=95, width=365, height=40)

movies_get_data = partial(get_recon_movies, user_input_dtype)

check_movies = tk.Button(root, text="Check Movies", font=('Bahnshcrift', 13, 'bold'),
                                    command=movies_get_data, bg='lawngreen', bd=3, fg='black')
check_movies.place(x=220, y=145, width=195)

exit_ = tk.Button(root, text="EXIT", font=('Bahnshcrift', 13, 'bold'), command=main_destroy, bg='black', bd=0,
                     fg='white')
exit_.place(x=265, y=400, width=95)

menu_top = tk.Menu(root)

# 1. Help menu option
in_help = tk.Menu(menu_top, tearoff=0)
in_help.add_command(label='Movies', command=dummy_inputs, font=('Bahnshcrift', 9))
menu_top.add_cascade(label='Help', menu=in_help)


# ----------------------- END OF ROOT WINDOW AND EVERYTHING -----------------------
root.config(menu=menu_top)
root.mainloop()
