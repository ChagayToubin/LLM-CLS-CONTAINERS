from Models.Manger import manger
class main:
    @staticmethod
    def start():
        m=manger()
        m.control_all()

if __name__ == "__main__":
    main.start()