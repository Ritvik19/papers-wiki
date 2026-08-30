# Trust Region and Proximal policy optimization (TRPO and PPO)

Sergios Karagiannakos on 2019-1-11 · 4 mins

**Source URL**: https://theaisummer.com/TRPO_PPO/

Policy gradient problems: high variance (actor-critic helps), delayed reward, sample inefficiency, learning rate sensitivity.

## TRPO

Constrain policy updates so new policy stays in a **trust region** where local approximations are accurate. KL divergence between new and old policy must be ≤ δ.

maximize_θ Ê_t[(π_θ(a_t|s_t) / π_θ_old(a_t|s_t)) Â_t]

subject to E_t[KL[π_θ_old(·|s_t), π_θ(·|s_t)]] ≤ δ

Solved with **conjugate gradient** (linear objective + quadratic constraint approximation). Steps: collect trajectories → estimate advantages → solve constrained problem → repeat.

## PPO (penalized form)

Incorporate KL constraint as penalty in objective instead of hard constraint → simple SGD. Coefficient C adapted based on KL magnitude.

## PPO-Clip (canonical)

Importance ratio r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t)

L^CLIP(θ) = Ê_t[min(r_t(θ)Â_t, clip(r_t(θ), 1−ε, 1+ε)Â_t)]

Clips advantage-weighted ratio when new policy diverges too far from old — prevents destructive large updates. Algorithm: collect trajectories → estimate advantages → multi-epoch SGD on clipped objective → repeat.
