package thejacketproject.Controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

/**
 * The main page controller.
 */
public class MainSceneController {
  private Stage primaryStage;

  public void setPrimaryStage(Stage primaryStage) {
    this.primaryStage = primaryStage;
  }

  @FXML
  private Pane buttonPane;

  @FXML
  private Button closetButton;

  @FXML
  private AnchorPane mainAnchorPane;

  @FXML
  private Pane standInPane;

  @FXML
  private Button userButton;

  @FXML
  void displayCloset(ActionEvent event) {

  }

  @FXML
  void goHome(ActionEvent event) {

  }

  @FXML
  void showProfile(ActionEvent event) {

  }

  public void switchPane(Pane newPane) {
    
  }

}
