# Track B Software Components Checklist
## Complete Installation & Setup Guide for Meta-Learning Orchestration on LeKiwi

**Platform:** LeKiwi mobile manipulator + Jetson Orin  
**OS:** Ubuntu 22.04 LTS (or 24.04)  
**Target:** Heterogeneous learning orchestration with LLM meta-learner  
**Status:** Pre-installation audit

---

## 1. CORE ROBOTICS STACK (Foundation)

### 1.1 ROS2 (Humble or Iron)
```bash
# Ubuntu 22.04 → ROS2 Humble (recommended for stability)
# Ubuntu 24.04 → ROS2 Iron (newer, experimental)
```
- **Package:** `ros-humble-desktop` or `ros-iron-desktop`
- **Dependencies:** gazebo, tf2, geometry_msgs, sensor_msgs
- **Why:** Core middleware for robot control, sensor fusion, planning
- **Installation time:** ~30 min
- **Disk space:** ~5 GB

### 1.2 LeKiwi Hardware Interface
- **LeKiwi driver package:** (check LeRobot GitHub or manufacturer)
  - Motor control (holonomic base + 5-DoF arm)
  - Feetech servo driver
  - Gripper control
  - IMU + encoder feedback
- **Alternative:** `ros2-feetech-driver` (community package)
- **Serial communication:** `python3-pyserial`
- **Installation time:** ~15 min
- **Note:** Verify LeKiwi firmware version compatibility

### 1.3 Gazebo (Simulation)
```bash
sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-gazebo-ros-control
```
- **Purpose:** Pre-hardware validation, control-loop testing
- **Models:** LeKiwi URDF + gripper
- **Physics engine:** ODE (Gazebo default) or Bullet
- **Installation time:** ~20 min
- **Disk space:** ~2 GB

### 1.4 NVIDIA Isaac Sim (Advanced Simulation)
```bash
# Download from NVIDIA Omniverse → Isaac Sim app
# Requires: RTX 3070+ GPU, 100 GB disk space
```
- **Purpose:** Photorealistic sensor simulation, domain randomization
- **Features:** Ray tracing, sensor noise injection, contact physics
- **ROS2 integration:** Isaac ROS packages (isaac_ros_image_proc, etc.)
- **Installation time:** ~45 min (download + setup)
- **Disk space:** ~100 GB
- **Hardware:** RTX 3070 minimum, RTX 4090 recommended

### 1.5 MoveIt2 (Motion Planning)
```bash
sudo apt install ros-humble-moveit
```
- **Purpose:** Trajectory planning, inverse kinematics for arm
- **Components:** Planning scene, collision detection, IK solvers
- **Configuration:** LeKiwi arm SRDF + kinematics config
- **Installation time:** ~20 min
- **Dependency:** ROS2 + Gazebo

---

## 2. VISION MODULE (Epistemic Uncertainty)

### 2.1 Deep Learning Framework
```bash
# PyTorch (recommended for uncertainty estimation)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
- **Version:** PyTorch 2.0+ with CUDA 11.8 support
- **Why:** Better for Bayesian/uncertainty methods than TensorFlow
- **Disk space:** ~5 GB
- **Installation time:** ~10 min

### 2.2 Uncertainty Quantification Libraries
```bash
pip install bayesian-torch batchbald gpytorch
pip install epistemic-uncertainty-pytorch
```
- **bayesian-torch:** MC-Dropout, Bayesian layers
- **batchbald:** Active learning uncertainty
- **gpytorch:** Gaussian processes
- **epistemic-uncertainty-pytorch:** Epistemic + aleatoric separation
- **Purpose:** Quantify confidence in vision predictions
- **Installation time:** ~5 min

### 2.3 Vision Libraries
```bash
pip install opencv-python opencv-contrib-python
pip install kornia  # differentiable vision operations
pip install albumentations  # image augmentation
```
- **opencv:** Image preprocessing, feature detection
- **kornia:** GPU-accelerated vision operations
- **albumentations:** Data augmentation for robustness
- **Installation time:** ~5 min

### 2.4 Foundation Model Backbones
```bash
pip install timm huggingface-hub transformers
```
- **timm (PyTorch Image Models):** ResNet, ViT, EfficientNet backbones
- **huggingface-hub:** Pre-trained foundation models (e.g., ViT-Base)
- **transformers:** Vision transformers, multimodal models
- **Purpose:** State-of-the-art vision backbones for LeKiwi perception
- **Installation time:** ~5 min (+ model download ~500 MB per model)

### 2.5 Camera & Sensor ROS Wrappers
```bash
sudo apt install ros-humble-usb-cam ros-humble-image-transport
```
- **usb_cam:** Standard USB camera interface
- **image_transport:** Efficient image publishing over ROS
- **Purpose:** Camera driver for LeKiwi's vision sensors
- **Installation time:** ~5 min

---

## 3. REINFORCEMENT LEARNING MODULE (Policy Variance)

### 3.1 RL Framework
```bash
pip install stable-baselines3[extra]
# OR for more advanced: pip install ray[rllib]
```
- **stable-baselines3:** Lightweight, tested (SAC, PPO, DDPG)
- **ray[rllib]:** Distributed RL, more features
- **Recommendation:** Start with stable-baselines3 (simpler), migrate to Ray if scaling needed
- **Installation time:** ~5 min
- **Disk space:** ~1 GB

### 3.2 SAC (Soft Actor-Critic) Implementation
```bash
# Included in stable-baselines3; just import
from stable_baselines3 import SAC
```
- **Why:** Off-policy, sample-efficient, entropy regularization enables uncertainty
- **Policy variance tracking:** Hook into policy entropy and Q-function variance
- **Installation time:** 0 min (included above)

### 3.3 RL Utilities
```bash
pip install gymnasium  # gym replacement (official)
pip install sb3-contrib  # additional algorithms
```
- **gymnasium:** Environment API, wrappers, monitoring
- **sb3-contrib:** QrdDQN, TQC, other algorithms
- **Installation time:** ~3 min

### 3.4 Simulation Environment Wrapper
```bash
pip install dm-control mujoco
```
- **dm-control:** DeepMind Control Suite (if using MuJoCo sim)
- **mujoco:** MuJoCo physics engine (alternative to Gazebo)
- **Purpose:** Fast RL training before real hardware
- **Installation time:** ~5 min
- **Optional:** Only if not using Gazebo + Isaac Sim

---

## 4. IMITATION LEARNING MODULE (Behavioral Fidelity)

### 4.1 Diffusion Policy (Main)
```bash
pip install diffusers einops omegaconf hydra-core
pip install timm pytorch-lightning
```
- **diffusers:** Diffusion model implementation (Hugging Face)
- **einops:** Efficient tensor operations
- **omegaconf + hydra-core:** Config management
- **timm:** UNet backbone for diffusion
- **pytorch-lightning:** Training loop abstraction
- **Installation time:** ~5 min

### 4.2 Behavioral Cloning (Baseline)
```bash
pip install imitation  # OpenAI Imitation Learning toolkit
# OR write custom BC using PyTorch
```
- **imitation:** Behavioral cloning, GAIL, other IL methods
- **Purpose:** Simple baseline for learning from demos
- **Installation time:** ~3 min

### 4.3 Decision Transformer (Alternative)
```bash
pip install decision-transformer
# OR clone from huggingface: https://huggingface.co/evals/gpt2-decision-transformer
```
- **decision-transformer:** Treats trajectory prediction as language model task
- **Purpose:** Transformer-based imitation learning
- **Installation time:** ~5 min

### 4.4 Trajectory & Demo Management
```bash
pip install h5py zarr pickle5
pip install dm-tree  # nested structure handling
```
- **h5py:** Store trajectories in HDF5 (efficient)
- **zarr:** Zarr format (streaming, chunked)
- **pickle5:** Python object serialization
- **dm-tree:** Nested dicts/lists (for multi-modal trajectories)
- **Installation time:** ~3 min

### 4.5 Human Demo Data Pipeline (LeRobot)
```bash
pip install lerobot
# OR: git clone https://github.com/huggingface/lerobot.git
```
- **lerobot:** Hugging Face robotics dataset library + training loops
- **Purpose:** Pre-trained models, demo datasets, unified training API
- **Installation time:** ~10 min

---

## 5. FAULT ADAPTATION MODULE (Recovery Success)

### 5.1 Meta-Learning Framework: MAML
```bash
pip install learn2learn
# OR clone: https://github.com/learnables/learn2learn
```
- **learn2learn:** MAML, ProtoNets, other meta-learning algorithms
- **Purpose:** Rapid adaptation to new faults within few gradient steps
- **Installation time:** ~3 min

### 5.2 Low-Rank Adaptation (LoRA)
```bash
pip install peft  # HuggingFace Parameter-Efficient Fine-Tuning
```
- **peft:** LoRA, QLoRA, prefix tuning, adapters
- **Why:** Efficient on-device fine-tuning without retraining full model
- **Installation time:** ~3 min
- **Dependency:** Transformers library

### 5.3 Quantization (if Jetson memory is critical)
```bash
pip install bitsandbytes  # QLoRA for quantized LoRA
pip install torch-quantization  # TorchScript quantization
```
- **bitsandbytes:** 8-bit optimization, QLoRA
- **torch-quantization:** Post-training quantization
- **Purpose:** Further reduce memory/latency on Jetson Orin
- **Installation time:** ~3 min
- **Optional:** Only if memory is bottleneck

### 5.4 Fault Detection & Diagnosis
```bash
pip install anomaly-detection-toolkit
# OR: pip install pytorch-forecasting (time-series anomaly detection)
```
- **anomaly-detection-toolkit:** Isolation Forest, One-Class SVM
- **pytorch-forecasting:** Temporal anomaly detection
- **Purpose:** Detect when fault has occurred
- **Installation time:** ~3 min

### 5.5 Replay Buffer & Episode Management
```bash
pip install d3rlpy  # Offline RL with replay buffers
# OR: pip install tianshou (replay buffer implementation)
```
- **d3rlpy:** Offline RL, replay buffers, episode utilities
- **tianshou:** Replay buffers, batch collection
- **Purpose:** Store episodes, sample for replay-based learning
- **Installation time:** ~3 min

---

## 6. LLM ORCHESTRATOR (Meta-Learning Coordinator)

### 6.1 Local LLM Inference Engine
```bash
pip install vllm
# OR: pip install ollama (simpler alternative)
# OR: pip install llamacpp-python (C++ backend for Jetson)
```
- **vllm:** Fast LLM inference with batching, quantization
- **ollama:** Simple local LLM runner (CLI + Python API)
- **llamacpp-python:** Lightweight, optimized for edge
- **Recommendation:** Start with `ollama` (easiest), move to `vllm` for speed
- **Installation time:** ~5 min

### 6.2 Small Language Models
```bash
# Download pre-trained models:
# Phi-2 (2.7B, quantized → ~1.5 GB)
# TinyLlama (1.1B, quantized → ~650 MB)
# Mistral 7B (quantized → ~4 GB)
# Llama 2 7B (quantized → ~4 GB)
```
- **ollama pull phi:2** or **ollama pull tinyllama**
- **or via Hugging Face Hub:**
  ```bash
  pip install huggingface-hub
  huggingface-cli download microsoft/phi-2 --local-dir ./models/phi-2
  ```
- **Purpose:** Core LLM running on Jetson Orin (~2-4W inference)
- **Installation time:** ~10-20 min (download varies by model size)
- **Disk space:** ~2-4 GB per model

### 6.3 LoRA Fine-Tuning for LLM
```bash
pip install peft transformers bitsandbytes
pip install unsloth  # Fast LoRA fine-tuning
```
- **peft:** LoRA layer management for LLM
- **unsloth:** Optimized LoRA fine-tuning (2-5× faster)
- **Purpose:** Online fine-tune LLM's allocation policy
- **Installation time:** ~5 min

### 6.4 Prompt Engineering & Structured Output
```bash
pip install guidance outlines
# OR: pip install instructor (for structured outputs via Pydantic)
```
- **guidance:** Constrained generation, structured prompts
- **outlines:** JSON schema-constrained sampling
- **instructor:** Pydantic integration for structured LLM outputs
- **Purpose:** Parse LLM decisions into machine-actionable allocation commands
- **Installation time:** ~3 min

### 6.5 LLM Utilities
```bash
pip install langchain  # LLM framework
pip install openai  # If using OpenAI API as fallback
```
- **langchain:** Chains, agents, memory management
- **openai:** Cloud fallback (if needed for debugging)
- **Installation time:** ~3 min
- **Optional:** Only if using langchain abstractions

---

## 7. HARDWARE-SPECIFIC (Jetson Orin)

### 7.1 NVIDIA CUDA Toolkit & cuDNN
```bash
# Pre-installed on Jetson; verify:
apt-cache policy cuda
apt-cache policy libcudnn8
```
- **CUDA:** 11.8 or 12.1 (check Jetson docs)
- **cuDNN:** 8.6+ for inference optimization
- **Purpose:** GPU acceleration for inference
- **Installation time:** 0 min (usually pre-installed)

### 7.2 TensorRT (Inference Optimization)
```bash
pip install tensorrt
# or: apt install tensorrt (system-wide)
```
- **Purpose:** Compile PyTorch/TensorFlow models to optimized NVIDIA format (~3-5× speedup)
- **Installation time:** ~5 min
- **Usage:** Convert models for deployment
- **Example workflow:**
  ```bash
  # Export PyTorch model to ONNX
  torch.onnx.export(model, dummy_input, "model.onnx", ...)
  # Compile to TensorRT
  trtexec --onnx=model.onnx --saveEngine=model.trt
  ```

### 7.3 Jetson Inference Libraries
```bash
pip install jetson-utils jetson-inference
# OR: git clone https://github.com/dusty-nv/jetson-inference
```
- **jetson-utils:** Image I/O, CUDA utilities
- **jetson-inference:** Pre-compiled models (ResNet, MobileNet, etc.)
- **Purpose:** Optimized inference for Jetson
- **Installation time:** ~10 min

### 7.4 Power & Thermal Monitoring
```bash
pip install jetson-stats  # Monitor GPU, CPU, power, temp
```
- **jetson-stats:** CLI tool for system monitoring
- **Purpose:** Track power consumption during multi-modality allocation
- **Installation time:** ~2 min

---

## 8. DATA MANAGEMENT & RECORDING

### 8.1 ROS2 Data Recording
```bash
sudo apt install ros-humble-rosbag2 ros-humble-rosbag2-storage-default-plugins
```
- **rosbag2:** Record/playback ROS topics (sensors, actions, metadata)
- **Purpose:** Collect training data for imitation learning
- **Installation time:** ~5 min

### 8.2 Episode & Trajectory Storage
```bash
pip install tensorboard tensorboard-plugin-profile
```
- **tensorboard:** Visualize training logs, episode rewards, adaptation curves
- **Installation time:** ~3 min

### 8.3 HDF5 & Data Format Libraries
```bash
pip install h5py zarr netcdf4 pandas polars
```
- **h5py:** Store trajectories in HDF5 (efficient for large datasets)
- **zarr:** Streaming, chunked storage
- **pandas/polars:** Tabular data (logs, metrics)
- **Installation time:** ~3 min

---

## 9. UTILITIES & DEVELOPMENT

### 9.1 Python Environment
```bash
python3 --version  # Should be 3.10+
pip install --upgrade pip setuptools wheel
python3 -m venv ~/track_b_env
source ~/track_b_env/bin/activate
```
- **Python 3.10+:** Required for many dependencies
- **Virtual environment:** Isolate project dependencies
- **Installation time:** ~5 min

### 9.2 Development Tools
```bash
pip install ipython jupyter jupyterlab
pip install black flake8 mypy pytest
pip install pre-commit
```
- **jupyter:** Interactive development, visualization
- **black/flake8/mypy:** Code quality, type checking
- **pytest:** Unit testing
- **Installation time:** ~5 min

### 9.3 Version Control
```bash
apt install git git-lfs
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
- **git:** Version control
- **git-lfs:** Large file storage (for data, models)
- **Installation time:** ~3 min

### 9.4 Documentation
```bash
pip install sphinx sphinx-rtd-theme mkdocs
pip install sphinx-autodoc-typehints
```
- **sphinx/mkdocs:** Generate documentation from docstrings
- **Installation time:** ~3 min

### 9.5 Logging & Monitoring
```bash
pip install loguru wandb tensorboard
```
- **loguru:** Structured logging (better than print)
- **wandb:** Experiment tracking (optional, cloud-based)
- **tensorboard:** Local experiment visualization
- **Installation time:** ~3 min

### 9.6 Visualization
```bash
pip install matplotlib seaborn plotly
pip install rviz2 rqt  # ROS2 visualization
```
- **matplotlib/seaborn/plotly:** Plotting
- **rviz2:** ROS2 3D visualization (robot pose, point clouds)
- **rqt:** ROS2 plugin GUI
- **Installation time:** ~5 min

---

## 10. OPTIONAL BUT RECOMMENDED

### 10.1 Quantization Tools (for faster inference)
```bash
pip install optimum auto-gptq
```
- **optimum:** HuggingFace model optimization
- **auto-gptq:** GPTQ quantization for LLMs
- **Purpose:** Reduce model size 4-8× with minimal accuracy loss
- **Installation time:** ~3 min

### 10.2 Mobile Robotics Benchmarks
```bash
pip install openai gym rtbs-benchmark  # Optional benchmark suites
```
- **Purpose:** Compare against standard robotics benchmarks
- **Installation time:** ~2 min
- **Optional:** Only for Paper 2 (transfer learning)

### 10.3 Space Robotics Simulation
```bash
# For space robotics validation (Paper 3 / Track A optional)
pip install ai4mars pykdl  # Mars terrain, kinematics
```
- **ai4mars:** Mars terrain dataset
- **pykdl:** Kinematics/dynamics library
- **Installation time:** ~3 min
- **Optional:** For space robotics domain extension

---

## 11. INSTALLATION SUMMARY

### Quick Install (30 min, minimal setup)
```bash
# 1. ROS2
sudo apt update && sudo apt install ros-humble-desktop

# 2. Python environment
python3 -m venv ~/track_b_env
source ~/track_b_env/bin/activate

# 3. Core ML stack
pip install torch torchvision stable-baselines3 peft transformers

# 4. Robotics
sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-moveit

# 5. LeKiwi-specific
git clone <lekiwi-driver-repo>

# 6. LLM
pip install ollama
ollama pull phi:2
```

### Full Install (2-3 hours, complete stack)
```bash
# Run all steps in Sections 1-9 above
# Recommended installation order:
# 1. ROS2 + Gazebo (foundation)
# 2. CUDA/cuDNN (Jetson)
# 3. PyTorch + deep learning
# 4. RL + imitation + meta-learning
# 5. LLM + local inference
# 6. Development tools
# 7. Optional tools
```

### Pre-Hardware Dev Setup (1 hour, laptop/desktop)
```bash
# Skip Sections 7 (Jetson-specific)
# Install Sections 1-6, 8-9
# Use Gazebo + Isaac Sim for simulation
# Code runs on CPU, migrate to Jetson later
```

---

## 12. VERIFICATION CHECKLIST

After installation, verify each component:

```bash
# 1. ROS2
source /opt/ros/humble/setup.bash
ros2 --version

# 2. PyTorch
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

# 3. Stable-Baselines3
python -c "from stable_baselines3 import SAC; print('SAC loaded')"

# 4. PEFT (LoRA)
python -c "from peft import LoraConfig; print('LoRA ready')"

# 5. LLM
ollama list  # or: vllm --version

# 6. LeKiwi drivers
ros2 pkg list | grep lekiwi  # Should show LeKiwi packages

# 7. MoveIt2
ros2 launch moveit_setup_assistant moveit_setup_assistant.launch.py

# 8. Gazebo
gazebo --version

# 9. Isaac Sim (if installed)
echo $ISAAC_SIM  # Should be set to Isaac Sim path
```

---

## 13. DEPENDENCY TREE (What Requires What)

```
Track B Thesis Root
├── ROS2 Humble (foundation)
│   ├── Gazebo + MoveIt2
│   ├── rosbag2 (data recording)
│   └── usb_cam (sensors)
│
├── Vision Module
│   ├── PyTorch + torchvision
│   ├── Epistemic uncertainty libs
│   └── Foundation models (timm, transformers)
│
├── RL Module
│   ├── Stable-Baselines3 (SAC)
│   ├── Gymnasium
│   └── Isaac Sim / MuJoCo (optional)
│
├── Imitation Learning
│   ├── Diffusion Policy
│   ├── LeRobot (huggingface)
│   └── Trajectory storage (h5py, zarr)
│
├── Fault Adaptation
│   ├── MAML (learn2learn)
│   ├── LoRA (peft)
│   └── Replay buffers (d3rlpy)
│
├── LLM Orchestrator
│   ├── Local LLM (vllm / ollama)
│   ├── Small models (Phi-2, TinyLlama)
│   ├── LoRA fine-tuning
│   └── Structured output (guidance, outlines)
│
├── Jetson Orin Hardware
│   ├── CUDA + cuDNN (pre-installed)
│   ├── TensorRT (optimization)
│   └── Jetson-specific libs
│
└── Dev Tools
    ├── Jupyter + IPython
    ├── Testing (pytest)
    ├── Logging (loguru, wandb)
    └── Visualization (matplotlib, rviz2)
```

---

## 14. FINAL SETUP STEPS FOR LEKIWI

### Once All Components Installed:

1. **Clone Track B repo (once created):**
   ```bash
   git clone <your-phd-repo> ~/track_b_thesis
   cd ~/track_b_thesis
   pip install -e .
   ```

2. **Download datasets:**
   ```bash
   # LeRobot demos
   huggingface-cli download HuggingFaceRobotics/lerobot-example-data
   
   # AI4Mars (if doing space robotics)
   # wget https://nasa-ai4mars-dataset.s3.amazonaws.com/...
   ```

3. **Set up LeKiwi URDF:**
   ```bash
   # Copy LeKiwi URDF to your workspace
   cp <lekiwi-models>/*.urdf ~/track_b_thesis/urdf/
   ```

4. **Launch LeKiwi in Gazebo (test):**
   ```bash
   ros2 launch lekiwi_gazebo bringup.launch.py
   ```

5. **Test LLM orchestrator initialization:**
   ```bash
   python ~/track_b_thesis/scripts/test_orchestrator.py
   ```

---

## 15. TROUBLESHOOTING QUICK LINKS

| Issue | Solution |
|---|---|
| CUDA not found | `conda install pytorch::pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia` |
| ROS2 packages not found | `source /opt/ros/humble/setup.bash` (or add to `~/.bashrc`) |
| PyTorch import errors | Ensure CUDA version matches PyTorch build; reinstall if mismatch |
| LeKiwi drivers not found | Clone repo and build: `colcon build --packages-select lekiwi_*` |
| LLM inference slow | Use TensorRT or GPTQ quantization; check Jetson power mode (`sudo nvpmodel -m 0`) |
| Out of memory | Enable swap on Jetson: `sudo fallocate -l 8G /swapfile` |
| Rosbag2 playback errors | Verify bag format: `rosbag2 info <bag_path>` |

---

**Total Installation Time:** 2–4 hours (depending on internet speed + hardware)  
**Total Disk Space:** ~120 GB (including Isaac Sim; ~20 GB without it)  
**Jetson Orin Memory Required:** 12 GB RAM minimum (32 GB ideal for comfort)

Ready to install? Start with Section 9.1 (Python environment), then proceed through Sections 1–6 in order.
