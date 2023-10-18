# try:
#     file= open("ganesh.txt","r+")
#     for i in file:
#         if i.isalpha or i.isspace:
#             print(i)
#     file.write("hello i am mani")
# except:
#     print("there is an erreor")


def clean_text(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

            cleaned_data = clean_operations(data)

        with open(output_file, 'w') as file:
            file.write(cleaned_data)

        print(f"Text data cleaned and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def clean_operations(text):
    cleaned_text = ' '.join(text.split("."))
    return cleaned_text


# Example usage:
input_file_path = 'input.txt'
output_file_path = 'cleaned_output.txt'
clean_text("ganesh.txt","cleandata.txt")



#output