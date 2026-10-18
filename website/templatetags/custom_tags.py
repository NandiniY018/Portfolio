from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

@register.filter(name='skill_gradient')
def skill_gradient(skill_name):
    name = (skill_name or '').lower().strip()
    if 'python' in name:
        return 'linear-gradient(90deg, #3776ab 0%, #ffd43b 100%)'
    elif name == 'c':
        return 'linear-gradient(90deg, #0284c7 0%, #38bdf8 100%)'
    elif 'html' in name:
        return 'linear-gradient(90deg, #e34f26 0%, #f97316 100%)'
    elif 'css' in name or 'tailwind' in name:
        return 'linear-gradient(90deg, #06b6d4 0%, #3b82f6 100%)'
    elif 'javascript' in name or 'js' in name:
        return 'linear-gradient(90deg, #f59e0b 0%, #fbbf24 100%)'
    elif 'react' in name:
        return 'linear-gradient(90deg, #06b6d4 0%, #38bdf8 100%)'
    elif 'django' in name:
        return 'linear-gradient(90deg, #059669 0%, #10b981 100%)'
    elif 'fast' in name:
        return 'linear-gradient(90deg, #0d9488 0%, #2dd4bf 100%)'
    elif 'next' in name:
        return 'linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%)'
    elif 'pandas' in name or 'numpy' in name:
        return 'linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%)'
    elif 'scikit' in name:
        return 'linear-gradient(90deg, #ea580c 0%, #f97316 100%)'
    elif 'power' in name:
        return 'linear-gradient(90deg, #d97706 0%, #f59e0b 100%)'
    elif 'eda' in name or 'exploratory' in name:
        return 'linear-gradient(90deg, #8b5cf6 0%, #ec4899 100%)'
    elif 'mysql' in name:
        return 'linear-gradient(90deg, #0284c7 0%, #0ea5e9 100%)'
    elif 'postgres' in name:
        return 'linear-gradient(90deg, #2563eb 0%, #38bdf8 100%)'
    elif 'mongo' in name:
        return 'linear-gradient(90deg, #16a34a 0%, #4ade80 100%)'
    elif 'sqlite' in name:
        return 'linear-gradient(90deg, #0284c7 0%, #38bdf8 100%)'
    elif 'git' in name:
        return 'linear-gradient(90deg, #e11d48 0%, #fb7185 100%)'
    elif 'docker' in name:
        return 'linear-gradient(90deg, #0284c7 0%, #38bdf8 100%)'
    elif 'postman' in name:
        return 'linear-gradient(90deg, #ea580c 0%, #f97316 100%)'
    elif 'code' in name or 'linux' in name:
        return 'linear-gradient(90deg, #0284c7 0%, #6366f1 100%)'
    return 'linear-gradient(90deg, #6366f1 0%, #a855f7 100%)'

@register.filter(name='category_meta')
def category_meta(category_name):
    cat = (category_name or '').lower().strip()
    if 'language' in cat:
        return {
            'icon': 'fas fa-code',
            'color': 'amber',
            'icon_bg': 'bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/20',
            'badge_bg': 'bg-amber-500/10 text-amber-700 dark:text-amber-300 border-amber-500/20',
            'glow_border': 'hover:border-amber-500/30 dark:hover:border-amber-500/30',
        }
    elif 'frontend' in cat:
        return {
            'icon': 'fab fa-react',
            'color': 'cyan',
            'icon_bg': 'bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 border-cyan-500/20',
            'badge_bg': 'bg-cyan-500/10 text-cyan-700 dark:text-cyan-300 border-cyan-500/20',
            'glow_border': 'hover:border-cyan-500/30 dark:hover:border-cyan-500/30',
        }
    elif 'backend' in cat:
        return {
            'icon': 'fas fa-server',
            'color': 'emerald',
            'icon_bg': 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/20',
            'badge_bg': 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border-emerald-500/20',
            'glow_border': 'hover:border-emerald-500/30 dark:hover:border-emerald-500/30',
        }
    elif 'data' in cat or 'ai' in cat:
        return {
            'icon': 'fas fa-brain',
            'color': 'purple',
            'icon_bg': 'bg-purple-500/10 text-purple-600 dark:text-purple-400 border-purple-500/20',
            'badge_bg': 'bg-purple-500/10 text-purple-700 dark:text-purple-300 border-purple-500/20',
            'glow_border': 'hover:border-purple-500/30 dark:hover:border-purple-500/30',
        }
    elif 'database' in cat:
        return {
            'icon': 'fas fa-database',
            'color': 'blue',
            'icon_bg': 'bg-blue-500/10 text-blue-600 dark:text-blue-400 border-blue-500/20',
            'badge_bg': 'bg-blue-500/10 text-blue-700 dark:text-blue-300 border-blue-500/20',
            'glow_border': 'hover:border-blue-500/30 dark:hover:border-blue-500/30',
        }
    else:
        return {
            'icon': 'fas fa-tools',
            'color': 'teal',
            'icon_bg': 'bg-teal-500/10 text-teal-600 dark:text-teal-400 border-teal-500/20',
            'badge_bg': 'bg-teal-500/10 text-teal-700 dark:text-teal-300 border-teal-500/20',
            'glow_border': 'hover:border-teal-500/30 dark:hover:border-teal-500/30',
        }
