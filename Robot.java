class Robot{
    String ref;
    String nom;
    int x;
    int y;
    int orientation;
    static int nbtotal;
    public final static int NORD = 1, EST = 2, SUD = 3, OUEST = 4;

    public Robot(String nom, int x, int y, int orientation){
        this.nom = nom;
        this.x = x;
        this.y = y;
        this.orientation = orientation;
        nbtotal += 1;
        this.ref = ("ROB" + nbtotal);
    }

    public Robot(String nom){
        this.nom = nom;
        this.x = 0;
        this.y = 0;
        this.orientation = 1;
        nbtotal += 1;
        this.ref = ("ROB" + nbtotal);
    }

    void modifOrientation(int orientation){
        this.orientation = orientation;
    }

    void deplacer(){
        if (this.orientation == 1 && x <= 0 && y <= 0) {
            this.y += 1;
        } else if (this.orientation == 2 && x <= 0 && y <= 0) {
            this.x += 1;
        } else if (this.orientation == 3 && x < 0 && y < 0) {
            this.y -= 1;
        } else if (this.orientation == 4 && x < 0 && y < 0) {
            this.x -= 1;
            }
        else {
            System.out.println("Le robot ne peut pas aller en négatif.");
        }
    }

    void afficheToi(){
        System.out.println(ref + ", " + nom + ", " + x + ", " + y + ", " + orientation);
    }
}