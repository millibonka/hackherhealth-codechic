package thejacketproject.controller;

import java.net.URL;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.AnchorPane;
import javafx.util.Pair;

/**
 * Class to load fxml file scenes in another scene.
 */
public class FxmlLoader {
  private AnchorPane view;

  /**
   * Return a new pane with loading an fxml file and getting the controller for it.
   *
   * @param fileName is the name of the loadable file
   * @return a Pair with the pane and its controller
   */
  public Pair<AnchorPane, Object> getPane(String fileName) {
    FXMLLoader loader = new FXMLLoader();
    try {
      URL fileUrl = getClass().getClassLoader().getResource(fileName + ".fxml");
      if (fileUrl == null) {
        throw new java.io.FileNotFoundException("FXML file cannot be found!");
      }
      loader.setLocation(fileUrl);
      view = loader.load();

    } catch (Exception e) {
      System.out.println("No page " + fileName + " found! Check FxmlLoader!");
      e.printStackTrace();
    }

    Object controller = loader.getController();
    return new Pair<>(view, controller);
  }
}

