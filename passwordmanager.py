import string

class PasswordManager:
    def __init__(self):
        self.l = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        self.num = len(self.l)

    def encrypt(self, p, key):
        c = ''
        for i in p:
            if not i == ' ':
                index = self.l.find(i)
                n = (index + key) % self.num
                c += self.l[n]
        return c

    def decrypt(self, c, key):
        p = ''
        for i in c:
            if not i == ' ':
                index = self.l.find(i)
                n = (index - key) % self.num
                p += self.l[n]
        return p

    def save_password(self, website, password, shift_key):
        password_data = f"{website}:{password}:{shift_key}\n"
        with open('passwords.dat', 'a') as file:
            file.write(password_data)

    def load_passwords(self):
        passwords = []
        with open('passwords.dat', 'r') as file:
            lines = file.readlines()
            for line in lines:
                try:
                    website, password, shift_key = line.strip().split(':')
                    password_data = {'website': website, 'password': password, 'shift_key': int(shift_key)}
                    passwords.append(password_data)
                except Exception as e:
                    print(e)
        return passwords

    def get_password(self, website):
        passwords = self.load_passwords()
        for password in passwords:
            if password['website'] == website:
                shift_key = password['shift_key']
                encrypted_password = password['password']
                decrypted_password = self.decrypt(encrypted_password, shift_key)
                return encrypted_password, decrypted_password
        return None, None

    def delete_password(self, website):
        passwords = self.load_passwords()
        new_passwords = []
        for password in passwords:
            if password['website'] != website:
                new_passwords.append(password)
        with open('passwords.dat', 'w') as file:
            for password in new_passwords:
                file.write(f"{password['website']}:{password['password']}:{password['shift_key']}\n")

    def display_passwords(self):
        passwords = self.load_passwords()
        for password in passwords:
            decrypted_password = self.decrypt(password['password'], password['shift_key'])
            print(f"Website: {password['website']}, Password: {decrypted_password}")

    def menu(self):
        while True:
            print("1) Encryption\n2) Decryption\n3) Save Password\n4) Get Password\n5) Delete Password\n6) Display Passwords\n7) Exit")
            x = int(input("Enter Choice: "))
            if x == 1:
                print("Encryption")
                password = input("Enter Password to encrypt: ")
                key = int(input("Enter shift key: "))
                encrypted_password = self.encrypt(password, key)
                print("Encrypted Password:", encrypted_password)
            elif x == 2:
                print("Decryption")
                encrypted_password = input("Enter Password to decrypt: ")
                key = int(input("Enter shift key: "))
                decrypted_password = self.decrypt(encrypted_password, key)
                print("Decrypted Password:", decrypted_password)
            elif x == 3:
                print("Save Password")
                website = input("Enter the website name: ")
                password = input("Enter the password: ")
                shift_key = int(input("Enter the shift key: "))
                self.save_password(website, password, shift_key)
            elif x == 4:
                print("Get Password")
                website = input("Enter the website name: ")
                encrypted_password, decrypted_password = self.get_password(website)
                if encrypted_password and decrypted_password:
                    print("Encrypted Password:", encrypted_password)
                    print("Decrypted Password:", decrypted_password)
                else:
                    print("No password found for the given website.")

            elif x == 5:
                print("Delete Password")
                website = input("Enter the website name: ")
                self.delete_password(website)
            elif x == 6:
                print("Display Passwords")
                self.display_passwords()
            elif x == 7:
                print("Bye Bye")
                break
            else:
                print("Invalid choice, please try again.")

passman = PasswordManager()
passman.menu()
