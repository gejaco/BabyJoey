from torchtnt.framework.callback import Callback
import torch

class Log(Callback):
    ######################## Training state #########################
    def on_train_start(self, state, unit) -> None:
        print("Training started!\n")

    def on_train_epoch_start(self, state, unit) -> None:
        print(f"Epoch {unit.train_progress.num_epochs_completed}!")
        
    def on_train_step_end(self, state, unit) -> None:
        if state.train_state and state.train_state.step_output:
            current_loss = state.train_state.step_output[0].item()  # Ensure step_output is valid
            # Print the batch number and the current loss, updating on the same line
            print(f"\rBatch {unit.train_progress.num_steps_completed_in_epoch}: Current Loss: {current_loss:.6f}", end="")
        else:
            # Print the "No valid loss" message on a new line
            print(f"Batch {unit.train_progress.num_steps_completed_in_epoch}: No valid loss available at this step.")

    ######################## Evaluation state #########################

    def on_eval_epoch_start(self, state, unit) -> None:
        # Log the start of an evaluation epoch
        print(f"\n")

    def on_eval_step_end(self, state, unit) -> None:
<<<<<<< HEAD
        if state.eval_state and state.eval_state.step_output:
            eval_loss = state.eval_state.step_output[0].item()  # Ensure step_output is valid
            # Print the evaluation step and the current loss
            print(f"\rEval Batch {unit.eval_progress.num_steps_completed}: Eval Loss: {eval_loss:.6f}", end="")
        else:
            print(f"Eval Batch {unit.eval_progress.num_steps_completed}: No valid loss available at this step.")
    
    def on_eval_epoch_end(self, state, unit) -> None:
        print(f"Evaluation epoch {unit.eval_progress.num_epochs_completed} ended!")    
    
=======
        step_input = unit.get_next_eval_batch(state, iter(state.eval_state.dataloader))
        
        # Check if 'input_ids' are available in step_input
        if 'input_ids' in step_input:
            input_ids = step_input['input_ids']
            
            # Create labels by shifting the input_ids to the right (causal language modeling)
            labels = input_ids[:, 1:].clone()  # Shift input_ids to create labels
            
            # Adjust input_ids to match the labels (remove the last token)
            input_ids = input_ids[:, :-1]
            
            # Retrieve the evaluation loss and logits from state.eval_state.step_output
            logits = state.eval_state.step_output[1]
            
            # Ensure logits are trimmed to match the length of the adjusted input_ids and labels
            logits = logits[:, :labels.size(1), :]  # Match logits size to labels
            
            # Get the predicted token (highest probability from logits)
            _, preds = torch.max(logits, dim=-1)
            
            # Check if there's a batch size mismatch between preds and labels
            if preds.size(0) != labels.size(0):
                min_size = min(preds.size(0), labels.size(0))
                preds = preds[:min_size]
                labels = labels[:min_size]
            
            # Calculate accuracy by comparing the predicted tokens to the shifted labels
            correct = torch.sum(preds == labels).item()
            total = labels.numel()  # Total number of tokens
            
            accuracy = correct / total * 100
            
            # Return the calculated accuracy
            print(f"\rEvaluation Accuracy: {accuracy:.2f}%", end="", flush=True)
        else:
            print("Warning: 'input_ids' not found in the step_input.")

>>>>>>> matty
    def on_eval_end(self, state, unit) -> None:
        print("\n")

    ######################## Exception Handling #########################
    def on_exception(self, state, unit, exc: BaseException) -> None:
        print(f"Exception occurred: {exc}")
<<<<<<< HEAD


# ------------- TODO Items for BabyJoey -------------:
# Training Loss: wandb.log({"train_loss": loss})
# Validation Loss: wandb.log({"val_loss": val_loss})
# Training Accuracy (for classification tasks): wandb.log({"train_accuracy": train_accuracy})
# Validation Accuracy (for classification tasks): wandb.log({"val_accuracy": val_accuracy})
# Perplexity (for language modeling): wandb.log({"perplexity": perplexity})
# Learning Rate: wandb.log({"learning_rate": lr})
# Epoch Number: wandb.log({"epoch": current_epoch})
# Step Number: wandb.log({"step": current_step})
# Gradient Norm: wandb.log({"gradient_norm": grad_norm})
# Optional Items for Transformers:
# Attention Weights/Maps: wandb.log({"attention_maps": attention_weights}) (if you want to visualize attention layers)
# Validation Metrics (e.g., F1, precision, recall for classification tasks):
# python
# Copy code
# wandb.log({
#     "val_f1": f1_score, 
#     "val_precision": precision, 
#     "val_recall": recall
# })
# Sample Predictions: wandb.log({"predictions": sample_predictions})
# Confusion Matrix (for classification tasks): wandb.log({"confusion_matrix": confusion_matrix})
# Throughput (Samples per second): wandb.log({"throughput": samples_per_sec})
# GPU/CPU Utilization: wandb.log({"gpu_usage": gpu_usage, "cpu_usage": cpu_usage})
# Model Checkpoints (e.g., every few epochs): wandb.save('model_checkpoint.pt')
# Tokenization Stats (optional, if interested in tokenization performance): wandb.log({"avg_tokens_per_sample": avg_tokens})
# For Language Models (additional logs):
# Perplexity (for language modeling): wandb.log({"perplexity": perplexity})
# Log Likelihood: wandb.log({"log_likelihood": log_likelihood})
=======
>>>>>>> matty