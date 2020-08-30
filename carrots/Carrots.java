import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStream;
public class Carrots {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        OutputStream os = new BufferedOutputStream(System.out);
        os.write(bf.readLine().split(" ")[1].getBytes());
        os.write('\n');
        os.flush();
        os.close();
    }

}

