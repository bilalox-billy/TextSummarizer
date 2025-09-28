from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
from datasets import load_from_disk


from src.textSummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        #load tokeniser
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        #load model
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collector = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir = self.config.root_dir,
            num_train_epochs = self.config.num_train_epochs,
            warmup_steps = self.config.warmup_steps,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size = self.config.per_device_eval_batch_size,
            weight_decay = self.config.weight_decay,
            logging_steps = self.config.logging_steps,
            eval_strategy = self.config.evaluation_strategy,
            eval_steps = self.config.eval_steps,
            save_steps = self.config.save_steps,
            gradient_accumulation_steps = self.config.gradient_accumulation_steps,
        )

        trainer = Trainer(
            model = model_pegasus,
            args = trainer_args,
            data_collator = seq2seq_data_collector,
            train_dataset = dataset_samsum_pt["train"],
            eval_dataset = dataset_samsum_pt["validation"],
            tokenizer = tokenizer
        )

        # Start training
        trainer.train()

        #save  the model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))

        # save the tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
