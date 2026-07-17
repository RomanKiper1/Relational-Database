# =============================================================================
# main.py — the graphical user interface (GUI) of the app.
#
# It builds a small desktop window with three tabs (Patients, Staff, Finance).
# For the data it does NOT touch PostgreSQL directly: it imports fetch_all and
# execute from db.py and lets that file handle all the database details.
# The GUI is built with customtkinter, a nicer-looking wrapper around Python's
# built-in "tkinter" toolkit.
# =============================================================================

import customtkinter as ctk               # the GUI library (aliased to "ctk" to type less)
from app.db import fetch_all, execute     # our own DB helpers from db.py

# --- Build the main window ------------------------------------------------
app = ctk.CTk()              # create the top-level application window
app.title("Clinic DB")       # text shown in the window's title bar
app.geometry("750x520")      # initial size: 750 pixels wide, 520 tall

# A "tab view" is the widget that shows several pages you can switch between.
tabs = ctk.CTkTabview(app, width=720, height=460)
# .pack() places the widget inside its parent. fill/expand make it grow with
# the window; padx/pady add 10px of empty space around it.
tabs.pack(padx=10, pady=10, fill="both", expand=True)

# Each .add() creates one tab page and returns the frame (container) for it.
# We keep those frames so we can put widgets inside each tab later.
patients_tab = tabs.add("Patients")
staff_tab = tabs.add("Staff")
finance_tab = tabs.add("Finance")
appointments_tab = tabs.add("Appointments")


# --- Data loaders: turn database rows into text lines ---------------------
# Each of these functions asks the DB for rows and returns a list of strings,
# one formatted line per row. The GUI code below just prints those strings.

def load_patients_lines():
    # fetch_all runs the SELECT and gives back a list of dict rows because of
    # RealDictCursor in db.py, so we can read columns by name: row["email"].
    from app.db import find_all

    rows = find_all("patients", sort=[("patient_id", 1)])
    lines = []

    for row in rows:
        # f-string with alignment "mini-language":
        #   {value:>3}   -> right-align in a field 3 chars wide  (nice for ids)
        #   {value:<15}  -> left-align  in a field 15 chars wide (columns line up)
        # \n at the end puts each patient on its own line.
        line = f"{row['patient_id']:>3} {row['first_name']} {row['last_name']:<15} {row['email']}\n"
        lines.append(line)
    return lines


def load_staff_lines():
    rows = find_all("staff", sort=[("staff_id", 1)])
    lines = []

    for row in rows:
        # Two adjacent string literals on separate lines are automatically
        # joined by Python into one string (no '+' needed).
        # `row['specialty'] or '-'` handles NULLs: in the DB non-doctors have
        # no specialty (Python sees None), and `None or '-'` gives '-' instead.
        line = (
            f"{row['staff_id']:>3}  {row['first_name']} {row['last_name']:<12}  "
            f"{row['role']:<15}  {(row['specialty'] or '-'):<12}  {row['email'] or ''}\n"
        )
        lines.append(line)
    return lines

def load_appoinments_lines():
    rows = find_all(
        "appointments",
        sort=[("appointment_date", 1), ("appointment_time", 1)],
    )
    
    lines = [
        f"{'ID': <5} {'Pat': <5} {'Doc':<12} {'Date':<12} {'Time':<10} {'Type':<14} Status\n",
        "-" * 70 + "\n",
    ]
    
    for row in rows:
        line = (
            f"{row['appointment_id']:<5}"
            f"{row['patient_id']:<5}"
            f"{row['staff_id']:<5}"
            f"{str(row['appointment_date']):<12}"
            f"{str(row['appointment_time']):<10}"
            f"{row['appointment_type']:<14}"
            f"{row['appointment_status']}\n"
        )
        lines.append(line)
    return lines


def load_finance_lines():
    # Placeholder: the finance tables don't exist yet, so we just return two
    # static lines of text instead of querying the database.
    return [
        "Finance tables not created yet.\n",
        "Add sql/04_schema_finance.sql when ready.\n",
    ]


# --- Pop-up dialog for adding a new patient -------------------------------
# `parent`   = the window this dialog belongs to.
# `on_saved` = a function to call AFTER a successful save (used to refresh the
#              list so the new patient appears immediately).
def add_patient_dialog(parent, on_saved):
    dialog = ctk.CTkToplevel(parent)   # a second, smaller window on top of the main one
    dialog.title("Add Patient")
    dialog.geometry("400x300")
    dialog.grab_set()                  # "modal": input goes to the dialog until it closes

    # Three text-entry fields. placeholder_text is the grey hint shown when empty.
    first_entry = ctk.CTkEntry(dialog, placeholder_text="First name", width=280)
    first_entry.pack(pady=5)
    first_entry.focus()                # put the text cursor here when the dialog opens

    last_entry = ctk.CTkEntry(dialog, placeholder_text="Last name", width=280)
    last_entry.pack(pady=5)

    email_entry = ctk.CTkEntry(dialog, placeholder_text="Email", width=280)
    email_entry.pack(pady=5)

    # This inner function runs when the user clicks "Save" or presses Enter.
    def save():
        # .get() reads the field's current text; .strip() removes surrounding spaces.
        first = first_entry.get().strip()
        last = last_entry.get().strip()
        # `... or None` turns an empty string "" into None, which becomes SQL NULL
        # (an empty email is stored as "no value" rather than an empty string).
        email = email_entry.get().strip() or None

        # Basic validation: first and last name are required. If missing, just
        # stop here (return) without saving.
        if not first or not last:
            return

        # INSERT the new patient. The %s are PLACEHOLDERS, not string formatting:
        # psycopg2 safely substitutes the tuple values (first, last, email),
        # which prevents SQL injection and handles types/NULL correctly.
        from app.db import insert_one, next_id

        insert_one("patients", {
            "patient_id": next_id("patients", "patient_id"),
            "first_name": first,
            "last_name": last,
            "email": email,
})

    # `command=save` connects the button click to the save() function above.
    ctk.CTkButton(dialog, text="Save", command=save).pack(pady=15)

    # Let the user press Enter (the "<Return>" key) to save from any field.
    # `lambda event: save()` is a tiny throwaway function; the key-binding
    # passes an event object we don't need, so we just ignore it and call save().
    dialog.bind("<Return>", lambda event: save())
    first_entry.bind("<Return>", lambda event: save())
    last_entry.bind("<Return>", lambda event: save())
    email_entry.bind("<Return>", lambda event: save())


# --- Generic tab builder (used by Staff and Finance) ----------------------
# `parent`  = the tab frame to fill.
# `load_fn` = one of the load_*_lines functions above. Passing a FUNCTION as an
#             argument lets one builder work for any data source ("callback").
def make_tab(parent, load_fn):
    # A textbox = a multi-line text area. We use a monospaced font (Consolas)
    # so the aligned columns from the f-strings line up correctly.
    textbox = ctk.CTkTextbox(
        parent, width=680, height=360,
        font=ctk.CTkFont(family="Consolas", size=13)
    )
    textbox.pack(padx=10, pady=10, fill="both", expand=True)

    def refresh():
        textbox.delete("1.0", "end")      # clear the box; "1.0" = line 1, char 0
        try:
            for line in load_fn():        # load_fn() runs the SELECT and returns lines
                textbox.insert("end", line)  # append each line at the end
        except Exception as exc:
            # If the DB query fails (e.g. table missing), show the error in the
            # textbox instead of crashing the whole program.
            textbox.insert("end", f"Error: {exc}\n")

    ctk.CTkButton(parent, text='Refresh', command=refresh).pack(pady=5)
    refresh()   # load data once immediately so the tab isn't empty on open



# --- Patients tab builder (adds an extra "Add Patient" button) ------------
# Almost the same as make_tab, but with a second button. (In a bigger project
# you'd merge these two into one function to avoid duplication.)
def make_patients_tab(parent, load_fn):
    textbox = ctk.CTkTextbox(parent, width=680, height=320, font=ctk.CTkFont(family="Consolas", size=13))
    textbox.pack(padx=10, pady=10, fill="both", expand=True)

    def refresh():
        textbox.delete("1.0", "end")
        try:
            for line in load_fn():
                textbox.insert("end", line)
        except Exception as exc:
            textbox.insert("end", f"Error: {exc}\n")

    # A frame is an invisible container; here it groups the two buttons so they
    # can sit side by side (side="left") on one row.
    btn_frame = ctk.CTkFrame(parent)
    btn_frame.pack(pady=5)

    ctk.CTkButton(btn_frame, text="Refresh", command=refresh).pack(side="left", padx=5)
    # `command=lambda: add_patient_dialog(parent, refresh)` opens the dialog and
    # passes `refresh` so the list reloads after a patient is saved. We wrap it
    # in a lambda because we need to pass arguments; `command` wants a function
    # to call later, not the result of calling it now.
    ctk.CTkButton(
        btn_frame, text="Add Patient",
        command=lambda: add_patient_dialog(parent, refresh)
    ).pack(side="left", padx=5)

    refresh()


# --- Wire the tabs to their data loaders ----------------------------------
make_patients_tab(patients_tab, load_patients_lines)  # patients tab has Add button
make_tab(staff_tab, load_staff_lines)                 # staff tab is read-only
make_tab(finance_tab, load_finance_lines)             # finance tab shows placeholder text
make_tab(appointments_tab, load_appoinments_lines)

# Start the GUI event loop. This line BLOCKS (keeps running) until the window
# is closed, listening for clicks, key presses, etc. Nothing after it runs
# until the app closes.
app.mainloop()
