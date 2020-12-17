from project_reader import ProjectReader


def main():
    while True:
        url = input("Project URL: ")

        if not url:
            break

        reader = ProjectReader(url)

        print("Project information:")
        print(reader.get_project())


if __name__ == "__main__":
    main()
