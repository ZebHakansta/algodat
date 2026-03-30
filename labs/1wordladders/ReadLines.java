import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class ReadLines {
    public static void main(String[] args) {
        String filePath = "example.txt";
        List<String> lista = new ArrayList<>();

        try (Stream<String> lines = Files.lines(Paths.get(filePath))) {
            lines.forEach();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}