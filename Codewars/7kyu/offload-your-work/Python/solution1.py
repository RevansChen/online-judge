# Python - 3.6.0

work_needed = lambda projectMinutes, freeLancers: (lambda t = projectMinutes - sum((h * 60 + m) for h, m in freeLancers): 'Easy Money!' if t <= 0 else f'I need to work {t // 60} hour(s) and {t % 60} minute(s)')()
