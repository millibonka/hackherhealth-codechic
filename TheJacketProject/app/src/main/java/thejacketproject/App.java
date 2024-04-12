package thejacketproject;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import thejacketproject.Controller.AppLaunchController;

/**
 * Opens the application.
 */
public class App extends Application {
  Stage primaryStage;

  @Override
  public void start(Stage primaryStage) throws Exception {

    // Load the FXML file
    FXMLLoader loader = new FXMLLoader(getClass().getResource("/fxml/LaunchScene.fxml"));
    Parent root = loader.load();

    // Get the controller instance
    AppLaunchController controller = loader.getController();
    controller.setPrimaryStage(primaryStage);

    // Set up the primary stage
    primaryStage.setTitle("The Jacket Project");
    primaryStage.setScene(new Scene(root, 335, 600));

    String  iconPath = "file:src/main/resources/images/jacket_icon.png";
    Image iconImage = new Image(iconPath);
    primaryStage.getIcons().add(iconImage);

    // Show the stage
    primaryStage.show();
  }

  public static void main(String[] args) {
    launch(args);
  }
}
