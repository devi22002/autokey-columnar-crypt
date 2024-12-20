import streamlit as st
import algoritma as crypto

def main():
    st.set_page_config(page_title="Enkripsi & Dekripsi", layout="centered")

    st.title("Program Enkripsi Dekripsi")
    st.subheader("Metode Autokey & Columnar")

    # Input teks asli
    message = st.text_input("Masukkan Teks Asli (Original Text):").upper()

    # Input kunci Autokey
    key_autokey = st.text_input("Masukkan Key Autokey: ").upper()

    # Input kunci Columnar
    key_columnar = st.text_input("Masukkan Key Columnar: ").upper()

    if st.button("Proses"):
        if message and key_autokey and key_columnar:
            # Proses enkripsi dan dekripsi
            key_new = crypto.generate_key(message, key_autokey)

            # Tabs untuk hasil
            tab1, tab2, tab3 = st.tabs(["Autokey Results", "Columnar Results", "Final Decryption"])

            with tab1:
                st.subheader("Autokey Results")
                cipher_autokey = crypto.encryptMessageAutokey(message, key_new)
                st.success(f"Cipherteks hasil Autokey: {cipher_autokey}")

            with tab2:
                st.subheader("Columnar Results")
                cipher_columnar = crypto.encryptMessageColumnar(message, key_columnar)
                st.success(f"Cipherteks hasil Columnar: {cipher_columnar}")

                final_cipher_text = crypto.encryptMessageColumnar(cipher_autokey, key_columnar)
                st.success(f"Cipherteks hasil Autokey & Columnar: {final_cipher_text}")

            with tab3:
                st.subheader("Final Decryption")

                # Dekripsi Columnar
                original_text = crypto.decryptMessageColumnar(final_cipher_text, key_columnar)
                st.info(f"Plainteks hasil dekripsi Columnar: {original_text}")

                # Dekripsi Autokey
                final_original_text = crypto.decryptMessageAutokey(original_text, key_new)
                st.info(f"Plainteks hasil dekripsi Columnar & Autokey: {final_original_text}")

    if st.button("Reset"):
        st.session_state.clear()

if __name__ == "__main__":
    main()
