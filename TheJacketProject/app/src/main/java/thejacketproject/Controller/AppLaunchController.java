package thejacketproject.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

/**
 * Opens the welcome scen to the homw scene.
 */
public class AppLaunchController {

  private Stage primaryStage;

  public void setPrimaryStage(Stage primaryStage) {
    this.primaryStage = primaryStage;
  }

  @FXML
  private Button getDressed;

  @FXML
  void openHome(ActionEvent event) throws Exception  {

    // Load the FXML file
    FXMLLoader loader = new FXMLLoader(getClass().getResource("/fxml/MainScene.fxml"));
    Parent root = loader.load();

    // Get the controller instance
    MainSceneController controller = loader.getController();
    controller.setPrimaryStage(primaryStage);

    Scene newScene = new Scene(root);
    primaryStage.setScene(newScene);

  }

}
