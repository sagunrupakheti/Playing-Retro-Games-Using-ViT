# This file is here just to define MlpPolicy/CnnPolicy
# that work for PPO
from stable_baselines3.common.policies import ActorCriticCnnPolicy, ActorCriticPolicy, MultiInputActorCriticPolicy, ActorCriticCustomCnnPolicy, ActorCriticCustomCnn2Policy

MlpPolicy = ActorCriticPolicy
CnnPolicy = ActorCriticCnnPolicy
MyPolicy = ActorCriticCustomCnnPolicy
MyPolicy2 = ActorCriticCustomCnn2Policy
MultiInputPolicy = MultiInputActorCriticPolicy
