#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Response Templates - NiTriTe V20.0
Templates structurés pour réponses ultra-détaillées
"""

from typing import Dict, List, Optional


class ResponseTemplates:
    """Templates pour réponses toujours très détaillées (5-10 paragraphes minimum)"""

    @staticmethod
    def format_list(items: List[str], prefix: str = "-") -> str:
        """Formate liste avec bullets"""
        return '\n'.join(f"{prefix} {item}" for item in items)

    @staticmethod
    def format_steps(steps: List[Dict]) -> str:
        """Formate étapes détaillées avec warnings/tips"""
        output = []
        for i, step in enumerate(steps, 1):
            output.append(f"\n**{i}. {step['action']}**")
            if 'details' in step:
                output.append(f"   {step['details']}")
            if 'warning' in step:
                output.append(f"   ⚠️ **Attention** : {step['warning']}")
            if 'tip' in step:
                output.append(f"   💡 **Astuce** : {step['tip']}")
            if 'expected' in step:
                output.append(f"   ✅ Résultat : {step['expected']}")
        return '\n'.join(output)

    def troubleshooting_template(self, problem: str, analysis: Dict, solutions: List[Dict],
                                 verification: List[str], nitrite_tools: List[Dict]) -> str:
        """
        Template troubleshooting ultra-détaillé

        Args:
            problem: Description problème
            analysis: {'causes': [], 'symptoms': [], 'severity': str}
            solutions: Liste de solutions détaillées
            verification: Étapes vérification
            nitrite_tools: Outils NiTriTe recommandés
        """
        tools_section = ""
        if nitrite_tools:
            tools_lines = []
            for tool in nitrite_tools:
                t = tool.get('tool', {})
                tools_lines.append(
                    f"- **{t.get('name', 'N/A')}** (NiTriTe → {tool.get('page', 'Diagnostic')})\n"
                    f"  {t.get('description', '')}"
                )
            tools_section = f"""
## 🛠️ Outils NiTriTe Recommandés

{chr(10).join(tools_lines)}
"""

        solutions_text = []
        for i, sol in enumerate(solutions, 1):
            priority_stars = "⭐" * sol.get('priority', 3)
            solutions_text.append(f"""
### Solution {i} : {sol['title']} {priority_stars}

**Difficulté** : {sol.get('difficulty', 'Moyenne')}
**Temps Estimé** : {sol.get('time', '10-15 minutes')}
**Efficacité** : {sol.get('effectiveness', 'Haute')}

#### Étapes Détaillées :
{self.format_steps(sol.get('steps', []))}

{'#### Commandes :' if sol.get('commands') else ''}
{f'```powershell{chr(10)}{sol.get("commands", "")}{chr(10)}```' if sol.get('commands') else ''}

**Résultat Attendu** : {sol.get('expected_result', 'Problème résolu')}
""")

        return f"""
# 🔍 Diagnostic : {problem}

## 1️⃣ Analyse du Problème

{analysis.get('description', '')}

**Causes Possibles** :
{self.format_list(analysis.get('causes', ['Analyse en cours...']))}

**Symptômes Observés** :
{self.format_list(analysis.get('symptoms', []))}

**Sévérité** : {analysis.get('severity', 'Moyenne')}

---

## 2️⃣ Solutions Détaillées (Par Ordre de Priorité)

{''.join(solutions_text)}

---

## 3️⃣ Vérification & Tests

Après avoir appliqué les solutions :

{self.format_list(verification, "✅")}

{tools_section}

---

## 4️⃣ Si Le Problème Persiste

**Prochaines étapes** :
- Vérifier tous logs système (NiTriTe → Logs)
- Test diagnostic complet (NiTriTe → Diagnostic)
- Consulter l'agent IA avec détails techniques précis

**Besoin d'aide supplémentaire ?** Demandez-moi avec les résultats des tests ci-dessus !
"""

    def optimization_template(self, goal: str, current_state: Dict, optimizations: List[Dict],
                             expected_gains: Dict) -> str:
        """Template optimisation système/gaming"""
        opt_text = []
        for i, opt in enumerate(optimizations, 1):
            opt_text.append(f"""
### Optimisation {i} : {opt['name']} ({opt.get('impact', 'Moyen')} impact)

{opt.get('description', '')}

**Actions** :
{self.format_steps(opt.get('steps', []))}

**Gain Attendu** : {opt.get('gain', '+5-10% performance')}
""")

        return f"""
# ⚡ Optimisation : {goal}

## État Actuel

{self.format_list([f"{k}: {v}" for k, v in current_state.items()])}

## Optimisations Recommandées

{''.join(opt_text)}

## Gains Totaux Attendus

{self.format_list([f"{k}: {v}" for k, v in expected_gains.items()])}

## Prochaines Étapes

1. Appliquer optimisations une par une
2. Tester après chaque modification
3. Mesurer gains réels avec outils NiTriTe → Diagnostic

**Note** : Gains peuvent varier selon configuration matérielle.
"""

    def general_detailed_template(self, question: str, answer_points: List[Dict],
                                  examples: List[str], related_topics: List[str]) -> str:
        """Template général détaillé (catch-all)"""
        points_text = []
        for i, point in enumerate(answer_points, 1):
            points_text.append(f"""
## {i}. {point['title']}

{point.get('content', '')}

{f'**Exemple** : {point.get("example", "")}' if point.get('example') else ''}
""")

        examples_text = f"""
## Exemples Concrets

{self.format_list(examples)}
""" if examples else ""

        related_text = f"""
## Sujets Connexes

{self.format_list(related_topics)}
""" if related_topics else ""

        return f"""
# {question}

{''.join(points_text)}

{examples_text}

{related_text}

---

**Besoin de précisions ?** N'hésitez pas à demander des détails sur un point spécifique !
"""


class TemplateFormatter:
    """Formateur appliquant templates aux réponses LLM"""

    def __init__(self):
        self.templates = ResponseTemplates()

    def apply_template(self, intent: str, llm_response: str, context: Dict) -> str:
        """
        Applique template approprié selon intent

        Args:
            intent: Type de query (troubleshooting, optimization, etc.)
            llm_response: Réponse brute du LLM
            context: Contexte (nitrite_tools, hardware, etc.)

        Returns:
            Réponse formatée avec template
        """
        # Pour l'instant, retourne réponse LLM enrichie avec outils NiTriTe
        nitrite_tools = context.get('nitrite_tools', [])

        if nitrite_tools:
            tools_section = "\n\n---\n\n## 🛠️ Outils NiTriTe Recommandés\n\n"
            for tool in nitrite_tools:
                t = tool.get('tool', {})
                page = tool.get('page', 'Diagnostic')
                tools_section += f"- **{t.get('name', 'N/A')}** (NiTriTe → {page})\n"
                tools_section += f"  {t.get('description', '')}\n\n"

            return llm_response + tools_section

        return llm_response


# Exemple d'utilisation
if __name__ == "__main__":
    templates = ResponseTemplates()

    # Test troubleshooting
    response = templates.troubleshooting_template(
        problem="PC Lent",
        analysis={
            'description': "Plusieurs facteurs peuvent causer des ralentissements",
            'causes': ["RAM saturée", "Disque plein", "Température élevée", "Malware"],
            'symptoms': ["Lag au démarrage", "Applications lentes", "Freeze aléatoires"],
            'severity': "Moyenne à Haute"
        },
        solutions=[
            {
                'title': "Nettoyage RAM et Services",
                'priority': 5,
                'difficulty': "Facile",
                'time': "5 minutes",
                'effectiveness': "Haute",
                'steps': [
                    {'action': "Ouvrir Gestionnaire Tâches", 'details': "Ctrl+Shift+Esc"},
                    {'action': "Trier par RAM", 'warning': "Ne pas fermer processus système"},
                    {'action': "Fermer apps lourdes", 'tip': "Discord, Chrome, etc."}
                ],
                'expected_result': "RAM < 70%"
            }
        ],
        verification=["Redémarrer PC", "Vérifier RAM usage", "Tester fluidité"],
        nitrite_tools=[]
    )

    print("=== Exemple Template Troubleshooting ===\n")
    print(response[:500] + "...\n")
