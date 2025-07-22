class clean:
    @staticmethod
    def clean_file(file):
        if "id" in file.columns:
            return file.drop(columns=['id'])
        else:
            return file