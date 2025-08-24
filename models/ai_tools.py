from odoo import models, fields, api
import random


class PredictionRendement(models.Model):
    _name = 'ai.prediction'
    _description = 'Prédiction de rendement'

    name = fields.Char(string='Nom', required=True)
    parcelle_id = fields.Many2one('parcelle.agri', string='Parcelle')
    culture_id = fields.Many2one('culture.agri', string='Culture')
    rendement_prevu = fields.Float(string='Rendement prédit')

    def action_calculer(self):
        for record in self:
            base = random.uniform(20.0, 60.0)
            record.rendement_prevu = round(base, 2)


class RecommandationOptimale(models.Model):
    _name = 'ai.recommandation'
    _description = 'Recommandation optimale'

    name = fields.Char(string='Nom', required=True)
    parcelle_id = fields.Many2one('parcelle.agri', string='Parcelle')
    culture_suggeree = fields.Char(string='Culture suggérée')
    raison = fields.Text(string='Raison')

    def action_recommander(self):
        for record in self:
            record.culture_suggeree = random.choice(['Blé', 'Maïs', 'Orge'])
            record.raison = 'Suggestion générée automatiquement.'


class DetectionStress(models.Model):
    _name = 'ai.stress'
    _description = 'Détection de stress'

    parcelle_id = fields.Many2one('parcelle.agri', string='Parcelle')
    type_stress = fields.Selection([
        ('hydrique', 'Stress hydrique'),
        ('climatique', 'Stress climatique'),
    ], string='Type de stress')
    niveau = fields.Float(string='Niveau (%)')

    def action_detecter(self):
        for record in self:
            record.niveau = round(random.uniform(0.0, 100.0), 2)


class SimulationScenario(models.Model):
    _name = 'ai.simulation'
    _description = 'Simulation de scénario'

    name = fields.Char(string='Nom', required=True)
    scenario = fields.Selection([
        ('rcp45', 'RCP 4.5'),
        ('rcp85', 'RCP 8.5'),
    ], string='Scénario')
    annee = fields.Integer(string='Année')
    impact_rendement = fields.Float(string='Impact sur rendement (%)')

    def action_simuler(self):
        for record in self:
            record.impact_rendement = round(random.uniform(-20.0, 20.0), 2)


class OptimisationRessource(models.Model):
    _name = 'ai.optimisation'
    _description = 'Optimisation des ressources'

    ressource = fields.Selection([
        ('eau', 'Eau'),
        ('engrais', 'Engrais'),
        ('main_oeuvre', "Main-d'œuvre"),
    ], string='Ressource')
    quantite_actuelle = fields.Float(string='Quantité actuelle')
    quantite_optimale = fields.Float(string='Quantité optimale')

    def action_optimiser(self):
        for record in self:
            if record.quantite_actuelle:
                record.quantite_optimale = round(record.quantite_actuelle * 0.9, 2)
            else:
                record.quantite_optimale = 0.0
